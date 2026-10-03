# ADR-003: Selección de PostgreSQL con Extensión PostGIS para Datos Geoespaciales

- **Estado**: Aceptado
- **Fecha**: 2026-09-30
- **Decisores**: Equipo de Desarrollo

## Contexto
El sistema requiere calcular prioridades por zonas geográficas, generar mapas de calor y realizar consultas espaciales (RF-02, RF-03).

## Alternativas Consideradas
1. **MongoDB (GeoJSON básico)**: Manejo flexible de documentos, pero consultas espaciales complejas limitadas.
2. **PostgreSQL + PostGIS**: Estándar de la industria para sistemas de información geográfica (GIS), consultas espaciales avanzadas e indexación R-Tree.

## Decisión
Usaremos **PostgreSQL + PostGIS**. Permite relacionar estructuras tabulares estructuradas con consultas geográficas optimizadas.

## Consecuencias
* **Positivas**: Alto rendimiento para renderizar miles de puntos geográficos y polígonos de zonas afectadas.
* **Negativas / Riesgos**: Mayor consumo de memoria RAM en el VPS; requiere optimización de índices espaciales (`GIST`).
