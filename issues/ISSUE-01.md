# Issue #01: Reportes duplicados al sincronizar desde modo sin conexión
**Reportado por:** Equipo de operaciones COER Arequipa  
**Observado:** Cuando un ciudadano envía un reporte con conexión inestable y la app móvil reintenta la sincronización con el mismo `cliente_uuid`, el sistema registra el reporte múltiples veces en la lista de reportes activos.  
**Esperado:** Si ya existe un reporte registrado con el mismo `cliente_uuid`, `registrar_reporte()` debe ignorar el duplicado y devolver el reporte existente sin duplicarlo.  
**Prueba que reproduce el error:**  
`tests/test_issue_01.py::test_issue_01_evita_reportes_duplicados_al_sincronizar`
