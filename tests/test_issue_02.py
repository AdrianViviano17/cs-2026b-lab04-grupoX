from src.reportes.servicio_sismos import calcular_prioridad_reporte


def test_issue_02_prioridad_critica_sin_foto():
    prioridad = calcular_prioridad_reporte(intensidad=8, heridos=2, tiene_foto=False)
    assert prioridad == "CRITICA"
