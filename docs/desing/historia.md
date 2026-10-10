# Historia de Usuario HU-08: Enviar y Sincronizar Reporte Sísmico Offline

**Como** ciudadano afectado por un sismo en Arequipa,
**Quiero** registrar un reporte de daños o emergencia sin necesidad de contar con conexión a Internet activa,
**Para** que el reporte se envíe y sincronice automáticamente con la central cuando la red se reestablezca.

## Criterios de Aceptación

1. **Dado** un usuario en una zona sin cobertura celular,
   **Cuando** completa los datos de la emergencia (ubicación GPS, nivel de daño) y presiona "Enviar",
   **Entonces** el reporte guarda el estado `ENCOLADO` localmente en la base de datos del dispositivo.

2. **Dado** un reporte en estado `ENCOLADO`,
   **Cuando** la aplicación detecta reconexión a Internet,
   **Entonces** el servicio sincroniza el reporte con el servidor central, cambiando su estado a `RECIBIDO`.
