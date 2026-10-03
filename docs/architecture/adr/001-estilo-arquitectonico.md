# ADR-001: Adopción de Monolito Modular con Ingesta Asíncrona para SismoReporta AQP

- **Estado**: Aceptado
- **Fecha**: 2026-09-30
- **Decisores**: Equipo de Desarrollo (3 integrantes)

## Contexto
Ante un evento sísmico masivo, la aplicación experimentará picos de hasta 20,000 reportes en la primera hora (QA-01). El proyecto cuenta con un equipo reducido de 3 desarrolladores (R-02) y debe desplegarse en 1 mes (R-01) sobre infraestructura económica (R-03).

## Alternativas Consideradas
1. Monolito en Capas Tradicional (3.80 en Matriz de Decisión)
2. Microservicios con Broker de Eventos (2.80 en Matriz de Decisión)
3. Monolito Modular con Ingesta Asíncrona via Redis (4.00 en Matriz de Decisión)

## Decisión
Aceptamos adoptar un **Monolito Modular con Ingesta Asíncrona**. Toda recepción de reportes se amortigua a través de una cola en memoria (Redis + Celery) antes de guardarse en la base de datos geográfica (PostgreSQL/PostGIS).

## Consecuencias
* **Positivas**: Absorción rápida de picos sin caída del servidor; fácil despliegue en un único VPS; separación modular de dominios (GIS, Reportes, Alertas).
* **Negativas / Riesgos**: Requiere asegurar consistencia eventual en la visualización inmediata del reporte mientras se procesa la cola.
