import pathlib

RAIZ = pathlib.Path(__file__).parent

def call_api(prompt, options, context):
    config = options.get("config", {})
    version = config.get("version", "v1")
    caso_id = context.get("vars", {}).get("id", "desconocido")
    
    ruta_grabacion = RAIZ / "grabaciones" / version / f"{caso_id}.txt"
    
    if not ruta_grabacion.exists():
        return {
            "error": f"No existe grabacion en {ruta_grabacion}. Ejecuta el prompt {version} para el caso {caso_id} y guarda la respuesta."
        }
        
    salida = ruta_grabacion.read_text(encoding="utf-8")
    return {"output": salida}
