# Comparación: Vista Dinámica C4 vs. Diagrama de Secuencia UML

## Diferencias en el nivel de detalle
1. **Omisión de detalles técnicos:** La vista dinámica de C4 omite detalles como activación de objetos, mensajes de respuesta síncronos/asíncronos, parámetros internos de métodos y el manejo de excepciones locales, enfocándose en la interacción de alto nivel entre componentes/contenedores.
2. **Público objetivo:** 
   - **Vista Dinámica C4:** Dirigida a arquitectos, líderes técnicos y desarrolladores para entender rápidamente el flujo global de datos durante la sincronización offline sin abrumarse con detalles sintácticos.
   - **Diagrama de Secuencia UML:** Dirigido a developers que van a codificar el flujo exacto en Python/JavaScript, mostrando métodos concretos (`guardar_localmente()`, `sincronizar()`), retornos y llamadas a métodos de dominio.
---

## Comparación: Modelado (Structurizr DSL) vs. Diagramación Manual (C4-PlantUML)

1. **Tiempo invertido:** La diagramación manual requiere escribir macros repetitivas por cada vista. Con Structurizr DSL se define cada elemento una sola vez y las 5 vistas se generan automáticamente.
2. **Errores de consistencia:** En la diagramación manual, un cambio en el nombre o tecnología de un contenedor exige modificar múltiples archivos individualmente, con alto riesgo de inconsistencias. En Structurizr DSL, actualizar el elemento en el modelo actualiza de inmediato todas las vistas exportadas.
