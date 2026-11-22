import pytest
from src.reportes.servicio_sismos import validar_coordenadas_arequipa


def test_issue_03_rechaza_coordenadas_fuera_de_arequipa():
    # Coordenadas de Lima (-12.04, -77.04) deben ser rechazadas
    with pytest.raises(ValueError):
        validar_coordenadas_arequipa(-12.04, -77.04)
