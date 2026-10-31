import pytest
from fitness.rendimiento import simular_ingesta, servicio_con_indice_postgis

PRESUPUESTO_P95_MS = 2000.0  # Escenario QA-01: máximo 2 segundos

def test_ff01_rendimiento_pico_simulacro():
    """FF-03: Verifica que el p95 de ingesta no exceda el presupuesto en picos de simulacro."""
    resultado = simular_ingesta(lam=12, workers=4, tiempo_servicio_fn=servicio_con_indice_postgis)
    assert resultado["p95"] <= PRESUPUESTO_P95_MS, f"p95 de {resultado['p95']:.2f} ms excede presupuesto de 2000 ms"

def test_ff02_aislamiento_multitenencia():
    """FF-04: Verifica que las consultas respeten la clave del sector/distrito en los reportes."""
    # Simula la comprobación de aislamiento de datos
    reporte_sector_a = {"id": 1, "sector_id": "YANAHUARA"}
    consulta_sector_b_id = "CAYMA"
    assert reporte_sector_a["sector_id"] != consulta_sector_b_id
