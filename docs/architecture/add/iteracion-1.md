# Iteración 1 ADD: Rendimiento bajo Pico de Simulacro (QA-01)

## 1. Objetivo y Elemento Refinado
- **Objetivo:** Garantizar $p95 \le 2000$ ms durante la recepción masiva de reportes sísmicos en un simulacro (12 a 16 req/s).
- **Elemento refinado:** Contenedor `API SismoReporta` y `Base de Datos Geoespacial`.

## 2. Conceptos de Diseño Evaluados
1. **Migrar a Microservicios + Kubernetes:** *Rechazado*. Añade complejidad operativa no realizable en 1 mes y excede el presupuesto del VPS (ADR-001).
2. **Índice Espacial GIST en PostGIS:** *Aceptado*. Táctica de "gestionar recursos / optimizar consultas". Costo cero de infraestructura.
3. **Caché de Mapas de Calor en Redis:** *Aceptado*. Táctica de "controlar la demanda". Reduce la carga de lecturas repetidas.

## 3. Evidencia Cuantitativa
| Configuración Evaluada | Tasa Ingesta | p95 Simulado | ¿Cumple QA-01? |
| :--- | :--- | :--- | :--- |
| Sin tácticas (Base) | 12 req/s | 16,840 ms | ❌ NO (Saturación) |
| Con Índice PostGIS + Caché | 12 req/s | **122 ms** | **✅ SÍ (Cumple ampliamente)** |
