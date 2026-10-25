# Auditoría de Calidad del Modelo C4 - SismoReporta AQP

| Vista | Pregunta / Criterio | Cumple (Sí/No) | Evidencia en el Modelo | Corrección / Observación |
| :--- | :--- | :--- | :--- | :--- |
| **Todas** | ¿Tienen título, alcance y descripción clara? | Sí | Definidos en cada bloque de vista en `workspace.dsl`. | N/A |
| **Contexto** | ¿Los elementos tienen nombre, tipo y descripción? | Sí | Se especifican Personas y Sistemas Externos etiquetados como "Externo". | N/A |
| **Contenedores** | ¿Cada contenedor especifica tecnología y protocolo en las relaciones? | Sí | `FastAPI`, `PostgreSQL 16 + PostGIS`, `Redis`, `HTTPS/JSON REST`, `SQL/TCP`. | N/A |
| **Componentes** | ¿Es coherente con el diagrama de paquetes del Lab 05? | Sí | Módulos de Ingesta, GIS, Brigadas e Infraestructura coinciden exactamente. | N/A |
| **Despliegue** | ¿Indica entorno, nodos anidados y presupuesto? | Sí | Especifica VPS Ubuntu 24.04 (2 vCPU, 4GB RAM) adecuado a presupuesto MVP. | N/A |

### Hallazgos de IA (Falsos Positivos Identificados)
- **Falso positivo reportado por IA:** La IA sugirió que la relación entre `Ciudadano` y `SismoReporta AQP` en Nivel 1 carecía de protocolo (`HTTPS`).
- **Verificación:** Según la lista oficial de C4 (Simon Brown), en el Nivel 1 (Contexto) **no se exige declarar protocolos tecnológicos** para usuarios humanos, ya que el público abarca perfiles no técnicos.
