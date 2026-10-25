class TwilioClient:
    """SDK externo de Twilio con su propia interfaz (retorna dict)."""
    def send_sms_message(self, to_phone: str, message: str) -> dict:
        if not to_phone or len(to_phone) < 9:
            return {"status": "error", "code": 400}
        return {"status": "sent", "sid": "SM123456789"}

class LocalSMSGateway:
    """SDK externo de módem local con interfaz distinta (retorna tupla de código y status)."""
    def dispatch(self, phone: str, text: str) -> tuple[int, str]:
        if not phone:
            return (500, "FAIL")
        return (200, "OK")
