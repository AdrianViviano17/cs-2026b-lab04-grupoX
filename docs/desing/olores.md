# Auditoría de Olores de Código - SismoReporta AQP (Lab 07)

| Líneas / Bloque | Fowler | Patrón GoF Propuesto | Principio SOLID Mejorado | Decisión del Equipo |
| :--- | :--- | :--- | :--- | :--- |
| `procesar_y_notificar` | **Método Largo / Complejidad Ciclomática Alta** (Radon CC > 12) | Strategy + Adapter | Single Responsibility / Open-Closed | **Aceptado:** Separar la lógica de envío SMS e IA. |
| Envío de SMS (`if/elif`) | **Acoplamiento a SDKs Externos** con interfaces heterogéneas | Adapter + Factory | Dependency Inversion | **Aceptado:** Crear adaptadores unificados para Twilio y SMS Local. |
| Reintentos duplicados | **Código Duplicado** en bloques try/catch por canal | Decorator | Open-Closed Principle | **Aceptado:** Envolver el despacho con `ConReintentos`. |
| `reporte.estado` | **Condicionales de Estado Anidados** | State Pattern | Single Responsibility | **Aceptado:** Reutilizar la máquina de estados del Lab 05. |
| `self.eventos.append` | **Acoplamiento Directo de Notificaciones** | Observer Pattern | Open-Closed / Single Responsibility | **Aceptado:** Implementar `PublicadorEventos`. |
| Instanciación de la Fábrica | Sugerencia de IA: usar **Singleton** en la fábrica | Singleton | Single Responsibility | **Rechazado:** Introduce estado global y complica la inyección en tests. |
