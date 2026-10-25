import pytest
import importlib

@pytest.fixture(params=["src.reportes.antes.servicio", "src.reportes.servicio"])
def modulo_servicio(request):
    return importlib.import_module(request.param)

def crear_reporte(m, desc="Derrumbe de vivienda en Yanahuara"):
    return m.Reporte(id_reporte=101, ciudadano_phone="954123456", descripcion=desc, lat=-16.40, lon=-71.53)

def test_procesar_reporte_exito_twilio(modulo_servicio):
    m = modulo_servicio
    srv = m.ServicioReportes()
    rep = crear_reporte(m)
    estado = srv.procesar_y_notificar(rep, canal_sms="TWILIO", proveedor_ia="LOCAL")
    assert estado == "VERIFICADO"
    assert rep.severidad == "ALTA"
    assert len(srv.eventos) == 2

def test_procesar_reporte_estado_invalido_lanza_error(modulo_servicio):
    m = modulo_servicio
    srv = m.ServicioReportes()
    rep = crear_reporte(m)
    rep.estado = "ATENDIDO"
    with pytest.raises(ValueError, match="El reporte ya fue atendido"):
        srv.procesar_y_notificar(rep, canal_sms="TWILIO")

def test_canal_sms_no_soportado_lanza_error(modulo_servicio):
    m = modulo_servicio
    srv = m.ServicioReportes()
    rep = crear_reporte(m)
    with pytest.raises(ValueError, match="no soportado"):
        srv.procesar_y_notificar(rep, canal_sms="WHATSAPP")
