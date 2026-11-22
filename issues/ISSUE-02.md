# Issue #02: Prioridad errónea cuando el reporte ciudadano no incluye foto
**Reportado por:** Coordinador de Defensa Civil - Cayma  
**Observado:** Reportes críticos con derrumbe o personas atrapadas (`intensidad >= 7` o `heridos > 0`) son degradados a prioridad `"MEDIA"` simplemente porque el campo `tiene_foto` es `False`.  
**Esperado:** La ausencia de fotografía no debe reducir la prioridad si existen indicadores de riesgo vital (`heridos > 0` o `intensidad >= 7`), debiendo clasificarse como `"CRITICA"`.  
**Prueba que reproduce el error:**  
`tests/test_issue_02.py::test_issue_02_prioridad_critica_sin_foto`
