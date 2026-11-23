import pathlib
import sys
from agentes.agente.herramientas import Herramientas
from agentes.agente.nucleo import Agente, ModeloGrabado
from agentes.agente.politica import Politica
from agentes.agente.traza import jsonl_a_mermaid

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TRAY = RAIZ / "agentes" / "trayectorias"
TRAZAS = RAIZ / "agentes" / "trazas"


def solicitar_aprobacion_humana(args: dict) -> bool:
    """Patrón Human-in-the-loop (E6): valida entrada estricta 's' o 'n'."""
    print(f"\n[HUMANO EN EL CIRCUITO] El agente propone editar: {args.get('ruta')}")
    while True:
        resp = input("¿Aprobar esta edición? (s/n): ").strip().lower()
        if resp in ("s", "n"):
            return resp == "s"
        print("Entrada inválida. Responda únicamente 's' o 'n'.")


def ejecutar_flujo_completo(modo_auto: bool = False):
    h = Herramientas(RAIZ)
    aprobador = None if modo_auto else solicitar_aprobacion_humana

    # 1. Issue #01 - Agente único ReAct (E2)
    ag1 = Agente(
        "agente_issue01",
        ModeloGrabado(TRAY / "issue_01.json"),
        h,
        Politica(max_pasos=12, aprobar_edicion=aprobador),
        "Resuelve issues/ISSUE-01.md",
        str(TRAZAS / "issue_01.jsonl"),
    )
    print("ISSUE 01:", ag1.ejecutar())
    jsonl_a_mermaid(TRAZAS / "issue_01.jsonl")

    # 2. Issue #02 - Multiagente Gestor + Actor-Crítico (E5)
    plan = (
        "1. Leer issues/ISSUE-02.md y reproducir test_issue_02.\n"
        "2. Corregir calcular_prioridad_reporte() en src/reportes/servicio_sismos.py.\n"
        "3. Verificar con pytest sin modificar tests/."
    )
    retro = ""
    for ronda in range(1, 3):
        ejecutor = Agente(
            f"ejecutor_r{ronda}",
            ModeloGrabado(TRAY / f"issue_02_ejecutor_r{ronda}.json"),
            h,
            Politica(max_pasos=12, aprobar_edicion=aprobador),
            f"Resuelve ISSUE-02.md siguiendo el plan:\n{plan}\n{retro}",
            str(TRAZAS / f"issue_02_ejecutor_r{ronda}.jsonl"),
        )
        resumen = ejecutor.ejecutar()
        jsonl_a_mermaid(TRAZAS / f"issue_02_ejecutor_r{ronda}.jsonl")

        revisor = Agente(
            f"revisor_r{ronda}",
            ModeloGrabado(TRAY / f"issue_02_revisor_r{ronda}.json"),
            h,
            Politica(
                herramientas_permitidas={"ver_cambios", "leer_archivo", "buscar", "ejecutar_pruebas"},
                max_pasos=8,
            ),
            f"Audita el cambio del ejecutor. Responde APROBADO o CAMBIOS SOLICITADOS.\nResumen: {resumen}",
            str(TRAZAS / f"issue_02_revisor_r{ronda}.jsonl"),
        )
        veredicto = revisor.ejecutar()
        jsonl_a_mermaid(TRAZAS / f"issue_02_revisor_r{ronda}.jsonl")
        print(f"ISSUE 02 (Ronda {ronda}) -> Revisor: {veredicto}")

        if not veredicto.startswith("CAMBIOS SOLICITADOS"):
            break
        retro = f"\nObservación del revisor: {veredicto}"

    # 3. Issue #03 - Agente con mapa_repo y memoria notas.md (E4)
    ag3 = Agente(
        "agente_issue03",
        ModeloGrabado(TRAY / "issue_03.json"),
        h,
        Politica(max_pasos=12, aprobar_edicion=aprobador),
        "Resuelve issues/ISSUE-03.md usando mapa_repo y notas.md",
        str(TRAZAS / "issue_03.jsonl"),
    )
    print("ISSUE 03:", ag3.ejecutar())
    jsonl_a_mermaid(TRAZAS / "issue_03.jsonl")


if __name__ == "__main__":
    ejecutar_flujo_completo(modo_auto="--auto" in sys.argv)
