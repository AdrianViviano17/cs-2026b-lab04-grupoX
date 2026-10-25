# Bitácora de Interacciones con IA Generativa - Lab 06

| Fecha | Herramienta | Prompt Generado | Propuesta de la IA | Verificación Humana / Decisión |
| :--- | :--- | :--- | :--- | :--- |
| 25/10/2026 | ChatGPT / Gemini | Generar borrador de Structurizr DSL para SismoReporta AQP | Incluyó un contenedor `Docker Compose` dentro del sistema. | **Corregido:** Docker Compose es infraestructura y pertenece a la vista de Despliegue, no es un contenedor C4. |
| 25/10/2026 | ChatGPT / Gemini | Proponer tecnologías para la cola asíncrona | Sugirió Apache Kafka para la ingesta. | **Rechazado:** Excede el plazo de 1 mes del MVP y contradice el ADR-001 (Redis). |
| 25/10/2026 | ChatGPT / Gemini | Generar relaciones entre componentes API | Generó dependencias circulares entre Ingesta y Brigadas. | **Corregido:** Se desacopló la relación usando el Módulo GIS como mediador para respetar la regla C4. |
| 25/10/2026 | ChatGPT / Gemini | Auditar vistas C4 con la lista oficial | Señaló falta de protocolos en relaciones de Personas Nivel 1. | **Descartado (Falso Positivo):** La norma C4 no requiere protocolos en relaciones con Personas en Nivel 1. |
| 25/10/2026 | ChatGPT / Gemini | Redactar explicación para público no técnico | Resumen inicial con jerga técnica (REST, PostGIS, PWA). | **Ajustado:** Se simplificó el texto a lenguaje comprensible en 115 palabras para autoridades municipales. |
