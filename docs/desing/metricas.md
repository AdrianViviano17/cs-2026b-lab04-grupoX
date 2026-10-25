# Reporte de Métricas de Refactorización - SismoReporta AQP

## 1. Comparativa de Complejidad Ciclomática (Radon) y SLOC

| Métrica | Antes (`antes/servicio.py`) | Después (`servicio.py` + módulos) | Impacto / Delta |
| :--- | :--- | :--- | :--- |
| **Complejidad Máxima (`procesar_y_notificar`)** | **14 (Riesgo Alto - Rango B)** | **2 (Excelente - Rango A)** | **-85.7% de complejidad** |
| **Complejidad Promedio del Módulo** | 7.5 | 1.4 | **-81.3% de complejidad** |
| **Líneas de Código Fuente (SLOC)** | 84 | 195 | +132% (Mayor modularidad) |
| **Número de Archivos / Módulos** | 1 archivo | 6 módulos desacoplados | Alta cohesión estructural |

## 2. Análisis del Trade-off
* **Lo que se ganó:** Complejidad ciclomática drásticamente reducida a un rango óptimo ($CC \le 2$). Posibilidad de añadir nuevos canales de mensajería (p. ej., WhatsApp) o proveedores de IA creando nuevas clases sin modificar el servicio principal (Cumplimiento estricto de Open/Closed).
* **El costo:** Incremento en las líneas de código totales y mayor nivel de indirección. El equipo debe conocer la estructura de patrones GoF.
* **Justificación de la versión:** Si el sistema únicamente fuera a soportar envío por Twilio y no requiriera IA ni cambio de estados, la versión ingenua habría bastado. Los patrones se justifican ante la evolución planificada del proyecto.
