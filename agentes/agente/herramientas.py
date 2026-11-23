import ast
import pathlib
import subprocess


class Herramientas:
    def __init__(self, raiz: str | pathlib.Path):
        self.raiz = pathlib.Path(raiz).resolve()
        self.ruta_notas = self.raiz / "agentes" / "notas.md"

    def catalogo(self) -> dict[str, str]:
        return {
            "listar_archivos": "listar_archivos(subruta='.') -> lista rutas relativas dentro del repositorio.",
            "leer_archivo": "leer_archivo(ruta) -> lee el contenido de texto de un archivo.",
            "buscar": "buscar(patron, subruta='src') -> busca texto en archivos .py o .md.",
            "editar_archivo": "editar_archivo(ruta, antes, despues) -> reemplaza un fragmento único en el archivo.",
            "ejecutar_pruebas": "ejecutar_pruebas(objetivo='tests') -> ejecuta pytest sobre la ruta indicada.",
            "ver_cambios": "ver_cambios() -> muestra git diff actual del repositorio.",
            "ejecutar_comando": "ejecutar_comando(comando) -> ejecuta un comando permitido (pytest, radon, git).",
            "mapa_repo": "mapa_repo(subruta='src') -> analiza el AST de Python y devuelve clases y firmas de funciones.",
            "anotar": "anotar(texto) -> guarda una hipótesis o archivo revisado en la memoria persistente notas.md.",
            "leer_notas": "leer_notas() -> recupera las notas almacenadas en notas.md durante la tarea.",
        }

    def _ruta(self, ruta: str) -> pathlib.Path:
        p = (self.raiz / ruta).resolve()
        if self.raiz not in p.parents and p != self.raiz:
            raise PermissionError(f"Ruta fuera del sandbox: {ruta}")
        return p

    def listar_archivos(self, subruta: str = ".") -> str:
        base = self._ruta(subruta)
        archivos = [
            str(p.relative_to(self.raiz)).replace("\\", "/")
            for p in sorted(base.rglob("*"))
            if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
        ]
        return "\n".join(archivos)

    def leer_archivo(self, ruta: str) -> str:
        return self._ruta(ruta).read_text(encoding="utf-8")

    def buscar(self, patron: str, subruta: str = "src") -> str:
        base = self._ruta(subruta)
        hallazgos = []
        for p in sorted(base.rglob("*.py")):
            for num, linea in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if patron in linea:
                    rel = str(p.relative_to(self.raiz)).replace("\\", "/")
                    hallazgos.append(f"{rel}:{num}: {linea.strip()}")
        return "\n".join(hallazgos) if hallazgos else "sin resultados"

    def editar_archivo(self, ruta: str, antes: str, despues: str) -> str:
        p = self._ruta(ruta)
        texto = p.read_text(encoding="utf-8")
        if texto.count(antes) != 1:
            return f"ERROR: el fragmento aparece {texto.count(antes)} veces; debe aparecer exactamente 1"
        p.write_text(texto.replace(antes, despues), encoding="utf-8")
        return f"OK: {ruta} modificado"

    def ejecutar_pruebas(self, objetivo: str = "tests") -> str:
        self._ruta(objetivo)
        res = subprocess.run(
            ["python", "-m", "pytest", "-q", objetivo],
            cwd=self.raiz,
            capture_output=True,
            text=True,
        )
        salida = (res.stdout + "\n" + res.stderr).strip()
        return salida or f"exit={res.returncode}"

    def ver_cambios(self) -> str:
        res = subprocess.run(
            ["git", "diff"], cwd=self.raiz, capture_output=True, text=True
        )
        return res.stdout.strip() or "(sin cambios)"

    def ejecutar_comando(self, comando: str) -> str:
        res = subprocess.run(
            comando.split(), cwd=self.raiz, capture_output=True, text=True
        )
        return (res.stdout + "\n" + res.stderr).strip()

    def mapa_repo(self, subruta: str = "src") -> str:
        """Herramienta nueva (E4): extrae estructura y firmas mediante AST sin leer archivos completos."""
        base = self._ruta(subruta)
        resumen = []
        for p in sorted(base.rglob("*.py")):
            rel = str(p.relative_to(self.raiz)).replace("\\", "/")
            arbol = ast.parse(p.read_text(encoding="utf-8"))
            items = []
            for nodo in arbol.body:
                if isinstance(nodo, ast.ClassDef):
                    metodos = [m.name for m in nodo.body if isinstance(m, ast.FunctionDef)]
                    items.append(f"class {nodo.name}({', '.join(metodos)})")
                elif isinstance(nodo, ast.FunctionDef):
                    args = [a.arg for a in nodo.args.args]
                    items.append(f"def {nodo.name}({', '.join(args)})")
            resumen.append(f"{rel}: {', '.join(items) if items else 'vacío'}")
        return "\n".join(resumen) if resumen else "sin módulos Python"

    def anotar(self, texto: str) -> str:
        """Memoria de notas/pizarra (E4): registra hipótesis y hallazgos en notas.md."""
        self.ruta_notas.parent.mkdir(parents=True, exist_ok=True)
        previo = self.ruta_notas.read_text(encoding="utf-8") if self.ruta_notas.exists() else "# Notas del Agente\n"
        self.ruta_notas.write_text(previo + f"- {texto.strip()}\n", encoding="utf-8")
        return "OK: nota guardada en notas.md"

    def leer_notas(self) -> str:
        """Recupera la memoria persistente de trabajo."""
        if not self.ruta_notas.exists():
            return "(sin notas previas)"
        return self.ruta_notas.read_text(encoding="utf-8")
