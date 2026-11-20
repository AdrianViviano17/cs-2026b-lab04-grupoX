import json
import pathlib
from typing import Protocol
from jsonschema import validate, ValidationError

RAIZ_REPO = pathlib.Path(__file__).resolve().parents[2]
RUTA_PROMPTS_A = RAIZ_REPO / "prompts" / "criterios"
RUTA_PROMPTS_B = RAIZ_REPO / "prompts" / "prioridad"

ESQUEMA_CRITERIOS = json.loads(
    (RUTA_PROMPTS_A / "asserts" / "esquema.json").read_text(encoding="utf-8")
)
ESQUEMA_PRIORIDAD = json.loads(
    (RUTA_PROMPTS_B / "asserts" / "esquema.json").read_text(encoding="utf-8")
)


class ProveedorLLM(Protocol):
    """Puerto del Laboratorio 07 para desacoplar el modelo de lenguaje."""
    def completar(self, prompt: str) -> str: ...


class SalidaInvalidaLLM(Exception):
    """Se lanza cuando la salida del LLM viola el JSON Schema (Capa 3 de defensa)."""


class GeneradorCriterios:
    def __init__(self, proveedor: ProveedorLLM, version: str = "v3"):
        self._proveedor = proveedor
        self.version = version
        self._plantilla = (RUTA_PROMPTS_A / f"{version}.txt").read_text(encoding="utf-8")

    def generar(self, historia_id: str, historia: str) -> dict:
        prompt = (
            self._plantilla
            .replace("{{id}}", historia_id)
            .replace("{{historia}}", historia)
        )
        respuesta_cruda = self._proveedor.completar(prompt)
        try:
            datos = json.loads(respuesta_cruda)
            validate(instance=datos, schema=ESQUEMA_CRITERIOS)
        except (json.JSONDecodeError, ValidationError) as exc:
            raise SalidaInvalidaLLM(
                f"Salida rechazada en {self.version}/{historia_id}: {exc}"
            ) from exc
        return datos


class ClasificadorPrioridadLLM:
    def __init__(self, proveedor: ProveedorLLM, version: str = "v3"):
        self._proveedor = proveedor
        self.version = version
        self._plantilla = (RUTA_PROMPTS_B / f"{version}.txt").read_text(encoding="utf-8")

    def clasificar(self, reporte_id: str, distrito: str, texto_reporte: str) -> dict:
        prompt = (
            self._plantilla
            .replace("{{id}}", reporte_id)
            .replace("{{distrito}}", distrito)
            .replace("{{texto_reporte}}", texto_reporte)
        )
        respuesta_cruda = self._proveedor.completar(prompt)
        try:
            datos = json.loads(respuesta_cruda)
            validate(instance=datos, schema=ESQUEMA_PRIORIDAD)
        except (json.JSONDecodeError, ValidationError) as exc:
            raise SalidaInvalidaLLM(
                f"Salida rechazada en {self.version}/{reporte_id}: {exc}"
            ) from exc
        return datos
