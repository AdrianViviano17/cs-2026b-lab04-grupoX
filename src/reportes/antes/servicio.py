import math
from src.reportes.externos import TwilioClient, LocalSMSGateway

class Reporte:
    def __init__(self, id_reporte: int, ciudadano_phone: str, descripcion: str, lat: float, lon: float):
        self.id = id_reporte
        self.phone = ciudadano_phone
        self.descripcion = descripcion
        self.lat = lat
        self.lon = lon
        self.estado = "BORRADOR"
        self.severidad = "INDETERMINADA"
        self.operacion_id = None

class ServicioReportes:
    def __init__(self, twilio_sdk=None, local_sms_sdk=None):
        self.twilio = twilio_sdk or TwilioClient()
        self.local_sms = local_sms_sdk or LocalSMSGateway()
        self.eventos = []

    def procesar_y_notificar(self, reporte: Reporte, canal_sms: str, proveedor_ia: str = "LOCAL") -> str:
        # Validar y cambiar estado (Condicionales anidados / Olor)
        if reporte.estado != "BORRADOR" and reporte.estado != "ENCOLADO":
            if reporte.estado == "ATENDIDO":
                raise ValueError("El reporte ya fue atendido")
            elif reporte.estado == "VERIFICADO":
                raise ValueError("El reporte ya está en proceso de atención")
            else:
                raise ValueError("Estado no válido para procesamiento")

        if not reporte.descripcion:
            raise ValueError("El reporte no tiene descripción del daño")

        # Asignación de severidad mediante IA (Condicionales mezclados)
        if proveedor_ia == "LOCAL":
            if "derrumbe" in reporte.descripcion.lower() or "atrapado" in reporte.descripcion.lower():
                reporte.severidad = "ALTA"
            else:
                reporte.severidad = "MEDIA"
        elif proveedor_ia == "LLM_MOCK":
            if len(reporte.descripcion) > 20:
                reporte.severidad = "ALTA"
            else:
                reporte.severidad = "BAJA"
        else:
            raise ValueError(f"Proveedor IA no soportado: {proveedor_ia}")

        reporte.estado = "RECIBIDO"

        # Envío de SMS con condicionales por proveedor (Olor)
        exito = False
        op_id = None
        if canal_sms == "TWILIO":
            for intento in range(3):
                try:
                    res = self.twilio.send_sms_message(reporte.phone, f"Alerta Sísmica: Severidad {reporte.severidad}")
                    exito = (res.get("status") == "sent")
                    op_id = res.get("sid")
                    if exito:
                        break
                except TimeoutError:
                    if intento == 2:
                        exito = False
        elif canal_sms == "SMS_LOCAL":
            for intento in range(3):
                try:
                    code, status = self.local_sms.dispatch(reporte.phone, f"Alerta Sísmica: Severidad {reporte.severidad}")
                    exito = (code == 200)
                    op_id = status
                    if exito:
                        break
                except TimeoutError:
                    if intento == 2:
                        exito = False
        else:
            raise ValueError(f"Canal SMS no soportado: {canal_sms}")

        if exito:
            reporte.estado = "VERIFICADO"
            reporte.operacion_id = op_id
            # Notificaciones acopladas "a mano"
            self.eventos.append(f"brigada_sms: {reporte.phone} -> Severidad {reporte.severidad}")
            self.eventos.append(f"tablero_defensa_civil: Reporte {reporte.id} VERIFICADO")
        else:
            reporte.estado = "ENCOLADO"

        return reporte.estado
