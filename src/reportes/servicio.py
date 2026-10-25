from src.reportes.estados import Borrador, Encolado
from src.reportes.estrategias import FabricaCanalesSMS, TwilioAdapter, LocalSMSAdapter
from src.reportes.eventos import PublicadorEventos, NotificadorBrigadas, ActualizadorTablero
from src.reportes.ia import ClasificadorLocal, ConCacheIA, GuardrailLongitudMinima, GuardrailLenguajeProhibido

class Reporte:
    def __init__(self, id_reporte: int, ciudadano_phone: str, descripcion: str, lat: float, lon: float):
        self.id = id_reporte
        self.phone = ciudadano_phone
        self.descripcion = descripcion
        self.lat = lat
        self.lon = lon
        self._estado_obj = Borrador()
        self.severidad = "INDETERMINADA"
        self.operacion_id = None

    @property
    def estado(self) -> str:
        return self._estado_obj.nombre

    def cambiar_estado(self, nuevo_estado):
        self._estado_obj = nuevo_estado

    def recibir(self): self._estado_obj.recibir(self)
    def verificar(self, op_id): self._estado_obj.verificar(self, op_id)

class ServicioReportes:
    def __init__(self):
        self.fabrica_sms = FabricaCanalesSMS()
        self.fabrica_sms.registrar("TWILIO", lambda: TwilioAdapter())
        self.fabrica_sms.registrar("SMS_LOCAL", lambda: LocalSMSAdapter())

        self.publicador = PublicadorEventos()
        self.eventos = []
        self.publicador.suscribir("reporte_verificado", NotificadorBrigadas(self.eventos))
        self.publicador.suscribir("reporte_verificado", ActualizadorTablero(self.eventos))

        self.clasificador_ia = ConCacheIA(ClasificadorLocal())
        self.guardrails = GuardrailLongitudMinima(GuardrailLenguajeProhibido())

    def procesar_y_notificar(self, reporte: Reporte, canal_sms: str, proveedor_ia: str = "LOCAL") -> str:
        # 1. Validar Guardrails
        self.guardrails.validar(reporte.descripcion)

        # 2. Transición de estado a RECIBIDO
        reporte.recibir()

        # 3. Inferencia de Severidad por IA
        reporte.severidad = self.clasificador_ia.clasificar_severidad(reporte.descripcion)

        # 4. Despacho SMS mediante Canal SMS
        canal = self.fabrica_sms.crear(canal_sms)
        res = canal.enviar_sms(reporte.phone, f"Alerta Sísmica: Severidad {reporte.severidad}")

        # 5. Confirmación de Estado y Eventos Observer
        if res.exito:
            reporte.verificar(res.operacion_id)
            self.publicador.publicar("reporte_verificado", {"id": reporte.id, "phone": reporte.phone, "severidad": reporte.severidad})
        else:
            reporte.cambiar_estado(Encolado())

        return reporte.estado
