# Informe de Comparación Round-Trip (Ingeniería Directa e Inversa)

Se comparó el diagrama de diseño manual (`clases.puml`) con el diagrama generado automáticamente mediante ingeniería inversa con `pyreverse` (`classes_reportes.puml`) sobre el código fuente en `src/reportes/`.

| Diferencia Observada | Causa Técnica | Acción Tomada |
| :--- | :--- | :--- |
| No aparece la composición explícita entre `Reporte` y `DetalleDanio`. | Limitación de `pyreverse` al interpretar listas tipadas en Python. | Se mantiene el diagrama de diseño original; se agregó una validación en código para exigir al menos un detalle de daño. |
| Ausencia de multiplicidades (`1`, `0..*`, `1..*`) en el diagrama generado. | El código en Python no expresa multiplicidades en su sintaxis nativa. | Documentado como limitación estándar del análisis estático de código. |
| Nombres de métodos en `snake_case` (`guardar_localmente`) frente a `camelCase` (`guardarLocalmente`) del diagrama. | Convención PEP 8 de Python frente a la notación UML estándar. | Se documenta la equivalencia de nombres respetando la regla C5. |
