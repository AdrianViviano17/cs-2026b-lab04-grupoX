from src.reportes.servicio_sismos import ReporteSismico, RepositorioReportes


def test_issue_01_evita_reportes_duplicados_al_sincronizar():
    repo = RepositorioReportes()
    r1 = ReporteSismico("uuid-101", "Cayma", 5, 0, True, -16.38, -71.54)
    r2 = ReporteSismico("uuid-101", "Cayma", 5, 0, True, -16.38, -71.54)

    repo.registrar_reporte(r1)
    repo.registrar_reporte(r2)

    assert len(repo.listar()) == 1
