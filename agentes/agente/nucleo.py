import json
import pathlib
import time
from typing import Protocol
from agentes.agente.contrato import validar_decision
from agentes.agente.politica import Politica


class Modelo(Protocol):
    def decidir(self, historial: list[dict]) -> dict: ...


class ModeloGrabado:
    """Reproduce decisiones JSON grabadas previamente."""
    def __init__(self, ruta_json: str | pathlib.Path):
        self.decisiones = json.loads(pathlib.Path(ruta_json).read_text(encoding="utf-8"))
        self.indice = 0

    def decidir(self, historial: list[dict]) -> dict:
        if self.indice >= len(self.decisiones):
            return {"pensamiento": "Fin de trayectoria grabada", "final": "Completado"}
        d = self.decisiones[self.indice]
        self.indice += 1
        return d


class ModeloInteractivo:
    """Permite operar con un asistente web sin clave de API y guarda la trayectoria."""
    def __init__(self, ruta_salida: str | pathlib.Path):
        self.ruta_salida = pathlib.Path(ruta_salida)
        self.grabadas = []

    def decidir(self, historial: list[dict]) -> dict:
        print("\n=== CONTEXTO PARA EL ASISTENTE ===")
        print(historial[-1]["content"])
        crudo = input("Pega la decisión JSON del asistente: ")
        decision = json.loads(crudo)
        self.grabadas.append(decision)
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        self.ruta_salida.write_text(json.dumps(self.grabadas, indent=2, ensure_ascii=False), encoding="utf-8")
        return decision


class Agente:
    def __init__(self, nombre: str, modelo: Modelo, herramientas, politica: Politica, objetivo: str, traza_archivo: str):
        self.nombre = nombre
        self.modelo = modelo
        self.h = herramientas
        self.politica = politica
        self.historial = [{"role": "user", "content": objetivo}]
        self.traza_archivo = pathlib.Path(traza_archivo)
        self.eventos: list[dict] = []
        self._t0 = 0.0

    def _registrar(self, **datos):
        datos["agente"] = self.nombre
        datos["t_ms"] = round((time.perf_counter() - self._t0) * 1000, 2)
        self.eventos.append(datos)

    def ejecutar(self) -> str:
        self._t0 = time.perf_counter()
        self._registrar(tipo="objetivo", estado="INICIO", texto=self.historial[0]["content"])
        conocidas = set(self.h.catalogo())

        for paso in range(1, self.politica.max_pasos + 2):
            d = self.modelo.decidir(self.historial)  # DECIDIENDO
            self.historial.append({"role": "assistant", "content": json.dumps(d, ensure_ascii=False)})
            ok, motivo = validar_decision(d, conocidas)  # VALIDANDO_CONTRATO

            if not ok:
                obs = f"ERROR DE CONTRATO: {motivo}. Responda solo con el JSON del protocolo."
                self._registrar(
                    tipo="accion", estado="CONTRATO_INVALIDO", paso=paso,
                    pensamiento=str(d)[:200], accion="(ninguna)", args={}, observacion=obs, bloqueada=True
                )
            elif "final" in d:
                self._registrar(
                    tipo="final", estado="FINALIZADO", paso=paso,
                    pensamiento=d["pensamiento"], texto=d["final"]
                )
                break
            else:
                accion, args = d["accion"], d.get("args", {})
                veredicto = self.politica.evaluar(accion, args, paso)  # EVALUANDO_POLITICA
                if veredicto.permitido:
                    try:
                        obs = getattr(self.h, accion)(**args)  # EJECUTANDO
                    except Exception as e:
                        obs = f"ERROR: {type(e).__name__}: {e}"
                    self._registrar(
                        tipo="accion", estado="OBSERVANDO", paso=paso,
                        pensamiento=d["pensamiento"], accion=accion, args=args,
                        observacion=str(obs)[:600], bloqueada=False
                    )
                else:
                    obs = f"BLOQUEADO POR LA POLÍTICA: {veredicto.motivo}"
                    limite = "máximo" in veredicto.motivo
                    self._registrar(
                        tipo="accion", estado="LIMITE_ALCANZADO" if limite else "BLOQUEADO",
                        paso=paso, pensamiento=d["pensamiento"], accion=accion, args=args,
                        observacion=obs, bloqueada=True
                    )
                    if limite:
                        break

            self.historial.append({"role": "user", "content": f"Observación: {obs}"})  # OBSERVANDO

        self.traza_archivo.parent.mkdir(parents=True, exist_ok=True)
        with open(self.traza_archivo, "w", encoding="utf-8") as f:
            for e in self.eventos:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        return self.eventos[-1].get("texto", "(sin respuesta final)")
