# Comparación: Vista Dinámica C4 vs. Diagrama de Secuencia UML

## Diferencias en el nivel de detalle
1. **Omisión de detalles técnicos:** La vista dinámica de C4 omite detalles como activación de objetos, mensajes de respuesta síncronos/asíncronos, parámetros internos de métodos y el manejo de excepciones locales, enfocándose en la interacción de alto nivel entre componentes/contenedores.
2. **Público objetivo:** 
   - **Vista Dinámica C4:** Dirigida a arquitectos, líderes técnicos y desarrolladores para entender rápidamente el flujo global de datos durante la sincronización offline sin abrumarse con detalles sintácticos.
   - **Diagrama de Secuencia UML:** Dirigido a developers que van a codificar el flujo exacto en Python/JavaScript, mostrando métodos concretos (`guardar_localmente()`, `sincronizar()`), retornos y llamadas a métodos de dominio.
