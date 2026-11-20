import pathlib
import re

BASE_DIR = pathlib.Path(__file__).resolve().parent


def call_api(prompt: str, options: dict, context: dict) -> dict:
    version = options.get("config", {}).get("version", "v3")
    vars_ctx = context.get("vars", {})
    reporte_id = vars_ctx.get("id")

    if not reporte_id:
        match = re.search(r"\b(REP-\d+)\b", prompt)
        reporte_id = match.group(1) if match else "REP-01"

    ruta_archivo = BASE_DIR / "grabaciones" / version / f"{reporte_id}.txt"
    if not ruta_archivo.exists():
        return {"error": f"No existe la grabacion: {ruta_archivo}"}

    salida = ruta_archivo.read_text(encoding="utf-8").strip()
    return {"output": salida}
