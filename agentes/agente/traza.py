import json
import pathlib
import sys


def jsonl_a_mermaid(ruta_jsonl: str | pathlib.Path) -> str:
    p = pathlib.Path(ruta_jsonl)
    eventos = [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
    lineas = ["sequenceDiagram", "    participant U as Usuario/Orquestador", "    participant A as Agente", "    participant P as Politica/Herramientas"]

    for ev in eventos:
        if ev["tipo"] == "objetivo":
            lineas.append("    U->>A: Objetivo asignado")
        elif ev["tipo"] == "accion":
            acc = ev["accion"]
            if ev.get("bloqueada"):
                lineas.append(f"    A-xP: {acc} (BLOQUEADO: {ev['estado']})")
            else:
                lineas.append(f"    A->>P: {acc}")
                lineas.append("    P-->>A: Observacion OK")
        elif ev["tipo"] == "final":
            lineas.append("    A-->>U: Respuesta final")

    salida_mmd = p.with_suffix(".mmd")
    contenido = "\n".join(lineas) + "\n"
    salida_mmd.write_text(contenido, encoding="utf-8")
    return contenido


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(jsonl_a_mermaid(sys.argv[1]))
