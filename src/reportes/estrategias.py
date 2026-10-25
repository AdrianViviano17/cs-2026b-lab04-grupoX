from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class ResultadoDespacho:
    exito: bool
    operacion_id: str | None = None

class CanalSMS(ABC):
    @abstractmethod
    def enviar_sms(self, telefono: str, mensaje: str) -> ResultadoDespacho:
        pass

# --- ADAPTERS ---
class TwilioAdapter(CanalSMS):
    def __init__(self, sdk=None):
        from src.reportes.externos import TwilioClient
        self._sdk = sdk or TwilioClient()

    def enviar_sms(self, telefono: str, mensaje: str) -> ResultadoDespacho:
        res = self._sdk.send_sms_message(telefono, mensaje)
        return ResultadoDespacho(exito=(res.get("status") == "sent"), operacion_id=res.get("sid"))

class LocalSMSAdapter(CanalSMS):
    def __init__(self, sdk=None):
        from src.reportes.externos import LocalSMSGateway
        self._sdk = sdk or LocalSMSGateway()

    def enviar_sms(self, telefono: str, mensaje: str) -> ResultadoDespacho:
        code, status = self._sdk.dispatch(telefono, mensaje)
        return ResultadoDespacho(exito=(code == 200), operacion_id=status)

# --- DECORATOR (Reintentos) ---
class ConReintentosSMS(CanalSMS):
    def __init__(self, interno: CanalSMS, intentos: int = 3):
        self._interno = interno
        self._intentos = intentos

    def enviar_sms(self, telefono: str, mensaje: str) -> ResultadoDespacho:
        for _ in range(self._intentos):
            try:
                res = self._interno.enviar_sms(telefono, mensaje)
                if res.exito:
                    return res
            except TimeoutError:
                continue
        return ResultadoDespacho(exito=False)

# --- FACTORY (Registro) ---
class FabricaCanalesSMS:
    def __init__(self):
        self._creadores = {}

    def registrar(self, nombre: str, creador_fn):
        self._creadores[nombre] = creador_fn

    def crear(self, nombre: str) -> CanalSMS:
        if nombre not in self._creadores:
            raise ValueError(f"Canal SMS no soportado: {nombre}")
        return ConReintentosSMS(self._creadores[nombre]())
