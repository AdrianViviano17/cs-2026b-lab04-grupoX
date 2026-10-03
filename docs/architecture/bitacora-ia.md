# Bitácora de Uso de Inteligencia Artificial - SismoReporta AQP

| # | Fecha | Herramienta | Prompt (Resumen) | Qué propuso la IA | Qué verificamos o corregimos | Decisión |
|---|---|---|---|---|---|---|
| 1 | 2026-09-29 | Gemini | Prompt RCRTF: Propuesta de 3 estilos arquitectónicos para 20k reportes/hora. | Recomendó Microservicios con Kafka por "escalabilidad ilimitada". | Inviable: R-01 (1 mes) y R-02 (3 dev) imposibilitan operar Kafka y 4 BDs. | **Rechazada** |
| 2 | 2026-09-29 | Gemini | Crítica adversarial sobre el Monolito Modular propuesto. | Detectó que el cuello de botella sería la escritura síncrona en BD durante la carga sísmica. | Se verificó correcto. Se agregó Redis/Celery como búfer asíncrono. | **Aceptada (Corregido)** |
| 3 | 2026-09-30 | Claude | Generación de sintaxis Mermaid para la arquitectura. | Diagrama con subgraphs y sintaxis válida en Mermaid v10. | Se corrigió la dirección de las flechas de infraestructura hacia Redis. | **Corregida** |
| 4 | 2026-09-30 | ChatGPT | Estrategia de mapas Offline para zonas sin internet. | Sugirió descargar tiles vectoriales completos de Arequipa (2GB). | Inviable para móviles de gama baja. Se ajustó a guardar solo datos de vectores livianos en GeoJSON. | **Corregida** |
| 5 | 2026-09-30 | GitHub Copilot | Generación de script en Python con la librería `diagrams`. | Código funcional para generar vista de despliegue. | Se agregaron iconos correctos de Redis y PostgreSQL con PostGIS. | **Aceptada** |

---

### Anexo: Prompts Utilizados

#### Prompt 1 (Generación de alternativas)
> **Rol**: Actúa como Arquitecto de Software Senior especializado en sistemas de emergencias y desastres.
> **Contexto**: Sistema "SismoReporta AQP" para recepción de reportes ciudadanos tras un sismo en Arequipa. 20,000 reportes en la primera hora con red celular colapsada.
> **Restricciones**: 3 desarrolladores, 1 mes de plazo, presupuesto de hosting bajo (VPS), app debe funcionar offline-first.
> **Tarea**: Propón 3 estilos arquitectónicos con ventajas, desventajas, riesgos y atributos que favorece/penaliza.
> **Formato**: Tabla comparativa en Markdown y recomendación final.

#### Prompt 2 (Crítica adversarial)
> **Rol**: Actúa como "abogado del diablo" y auditor de arquitectura.
> **Tarea**: Critica la arquitectura de Monolito Modular elegida. ¿Qué fallará exactamente cuando ingresen 20,000 reportes en la primera hora en un VPS económico? Detalla 3 riesgos críticos y tácticas de mitigación.
