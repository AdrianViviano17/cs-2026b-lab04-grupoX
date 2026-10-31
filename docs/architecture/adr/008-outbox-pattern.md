# ADR 008: Garantía de Entrega de Eventos sin Pérdida mediante Patrón Outbox y Publicador Asíncrono

* **Estado:** Aceptado
* **Contexto:** 
  En el escenario de disponibilidad **QA-02**, el sistema debe garantizar un **0% de pérdida de datos/eventos** en caso de que la red falle o los microservicios consumidores de alertas sufran caídas momentáneas durante el colapso de la infraestructura tras un sismo. La publicación directa de eventos en memoria (Observer síncrono) arriesga la pérdida irrecuperable de notificaciones si la ejecución falla a mitad del proceso.
* **Decisión:** 
  Implementar el patrón **Transactional Outbox**. Las notificaciones y eventos generados (`reporte_verificado`) se escriben dentro de la misma transacción de base de datos donde se persiste el reporte principal en una tabla `outbox_events`. Un proceso worker asíncrono secundario consulta periódicamente esta tabla, despacha los eventos hacia los canales/suscriptores y marca su estado como procesado tras recibir la confirmación de recepción (ACK).
* **Consecuencias:** 
  * **Positivas:** Garantía de entrega *at-least-once* con resiliencia total a fallos de red o caídas de servicios externos, manteniendo desacoplada la persistencia principal del envío de notificaciones.
  * **Negativas:** Mayor complejidad operacional al requerir un worker asíncrono dedicado en segundo plano y posibilidad de recibir eventos duplicados en los consumidores (requiere idempotencia en la recepción).
