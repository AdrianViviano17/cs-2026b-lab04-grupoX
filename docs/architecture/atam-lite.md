# Evaluación de Arquitectura ATAM-Lite - SismoReporta AQP

## 1. Matriz de Hallazgos
- **Punto de Sensibilidad:** El $p95$ durante la ingesta en simulacros depende de la correcta aplicación del índice GIST en PostGIS.
- **Punto de Trade-off:** El almacenamiento offline (*Outbox*) garantiza **Disponibilidad (0% pérdida de datos)** a costa de **Consistencia Eventual** (demora de hasta 5 min en reflejarse en el tablero central).
- **Riesgo R1 (Aceptado):** Servidor VPS único representa un punto único de falla (*SPOF*). Se acepta por restricción de presupuesto (MVP).
- **No Riesgo:** El Monolito Modular en Python/FastAPI soporta holgadamente la carga requerida sin migrar a microservicios.
