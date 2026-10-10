# Bitácora de Interacciones con la IA (Lab 05)

| Fecha | Herramienta | Prompt Principal | Propuesta de la IA | Verificación y Decisión |
| :--- | :--- | :--- | :--- | :--- |
| 06/10/2026 | ChatGPT / Claude | Generar diagrama de clases PlantUML para HU-08 de SismoReporta AQP. | Propuso una relación de herencia entre `Reporte` y `DetalleDanio`. | **Rechazada**: Se corrigió a Composición `Reporte "1" *-- "1..*" DetalleDanio`. |
| 07/10/2026 | Copilot / Claude | Generar diagrama de secuencia para sincronización offline de reportes. | Incluyó llamadas sincrónicas directas al servidor sin guardar localmente. | **Corregida**: Se adaptó para incluir guardado en repositorio local e iteración en reconexión. |
| 08/10/2026 | ChatGPT / Gemini | Convertir el ciclo de vida de `Reporte` a diagrama Mermaid. | Propuso estados `BORRADOR`, `ENCOLADO`, `RECIBIDO`, `VERIFICADO`, `ATENDIDO`. | **Aceptada**: Coincide plenamente con la enumeración `EstadoReporte`. |
| 09/10/2026 | Claude / Copilot | Generar esqueleto de código en Python a partir de `clases.puml`. | Generó clases con `dataclasses` y métodos con `raise NotImplementedError`. | **Aceptada**: Se guardó la estructura base en `src/reportes/dominio.py`. |
| 10/10/2026 | ChatGPT / Gemini | Auditar consistencia C1-C5 de los diagramas entregados. | Detectó 2 inconsistencias reales y 2 falsos positivos. | **Verificada**: Se aplicaron las correcciones reales y se documentó en `consistencia.md`. |
