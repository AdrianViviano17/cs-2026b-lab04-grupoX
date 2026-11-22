from dataclasses import dataclass


@dataclass
class ReporteSismico:
    cliente_uuid: str
    distrito: str
    intensidad: int
    heridos: int
    tiene_foto: bool
    latitud: float
    longitud: float
    prioridad: str = "BAJA"


class RepositorioReportes:
    def __init__(self):
        self._reportes: list[ReporteSismico] = []

    def listar(self) -> list[ReporteSismico]:
        return list(self._reportes)

    def registrar_reporte(self, reporte: ReporteSismico) -> ReporteSismico:
        # BUG ISSUE-01: No verifica si cliente_uuid ya fue sincronizado anteriormente
        validar_coordenadas_arequipa(reporte.latitud, reporte.longitud)
        reporte.prioridad = calcular_prioridad_reporte(
            reporte.intensidad, reporte.heridos, reporte.tiene_foto
        )
        self._reportes.append(reporte)
        return reporte


def calcular_prioridad_reporte(intensidad: int, heridos: int, tiene_foto: bool) -> str:
    # BUG ISSUE-02: Si no tiene foto, degrada erróneamente a MEDIA incluso con heridos o intensidad alta
    if not tiene_foto:
        return "MEDIA"
    if heridos > 0 or intensidad >= 7:
        return "CRITICA"
    if intensidad >= 5:
        return "ALTA"
    return "BAJA"


def validar_coordenadas_arequipa(latitud: float, longitud: float) -> bool:
    # BUG ISSUE-03: No valida el rango geográfico de Arequipa (-17.5 a -14.5 lat, -75.2 a -70.8 lon)
    if latitud is None or longitud is None:
        raise ValueError("Coordenadas requeridas")
    return True
