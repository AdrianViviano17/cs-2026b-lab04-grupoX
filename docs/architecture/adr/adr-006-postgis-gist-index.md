# ADR 006: Inserción de Coordenadas mediante PostGIS con Indexación Espacial (GiST)

* **Estado:** Aceptado
* **Contexto:** 
  Durante un evento sísmico masivo, la meta cuantitativa del escenario QA-01 exige procesar hasta 20,000 reportes por hora manteniendo una latencia en el percentil 95 ($p95 \le 2.0\text{ s}$). Las búsquedas y consultas de densidad espacial en tablas relacionales convencionales provocan escaneos secuenciales que degradan severamente el rendimiento del sistema.
* **Decisión:** 
  Adoptar la extensión espacial **PostGIS** sobre PostgreSQL y aplicar un índice de árbol de búsqueda espacial de tipo **GiST** (`Generalized Search Tree`) sobre la columna geográfica de ubicación de los reportes.
* **Consecuencias:** 
  * **Positivas:** Optimización drástica en el tiempo de respuesta de las consultas espaciales por rango y densidad, garantizando que tanto la persistencia como las lecturas agregadas se mantengan bajo el umbral $p95 \le 2.0\text{ s}$ durante picos de tráfico masivo.
  * **Negativas:** Incremento en el consumo de almacenamiento en disco y sobrecarga adicional de memoria RAM para la actualización y mantenimiento del árbol GiST durante ráfagas de escritura simultáneas.
