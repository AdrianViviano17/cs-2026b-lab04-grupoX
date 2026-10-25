# ADR-005: Adopción de Patrones de Diseño GoF en Módulo de Ingesta

**Estado:** Aceptado (25/10/2026)

## Contexto
El método principal `procesar_y_notificar` presentaba una complejidad ciclomática de 14. La incorporación de nuevos servicios de SMS o componentes de IA requería modificar la lógica central, violando el principio Open/Closed.

## Decisión
1. Adoptar **Strategy + Adapter + Factory Method** para aislar SDKs externos (Twilio, SMS Local).
2. Adoptar **State Pattern** para gestionar las transiciones de estado del reporte.
3. Adoptar **Observer Pattern** para desacoplar el envío de alertas y notificaciones a tableros.
4. Adoptar **Chain of Responsibility + Decorator** para aislar el componente de IA y aplicar guardrails de seguridad.
5. Rechazar el patrón **Singleton** en las fábricas para evitar estado global e higienizar los tests.

## Consecuencias
* (+) Reducción de la complejidad ciclomática de 14 a 2.
* (+) Inyección de dobles de prueba para componentes de IA sin consumo de APIs reales.
* (-) Aumento en la cantidad de clases y archivos dentro del repositorio.
