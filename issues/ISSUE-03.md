# Issue #03: Se aceptan coordenadas fuera del departamento de Arequipa
**Reportado por:** Analista GIS - SismoReporta AQP  
**Observado:** El validador geográfico acepta reportes con coordenadas en Lima u otros países (ej. latitud `-12.04`, longitud `-77.04`) sin rechazarlos.  
**Esperado:** Solo deben aceptarse coordenadas dentro del cuadro delimitador de Arequipa (`latitud` entre `-17.5` y `-14.5`, `longitud` entre `-75.2` y `-70.8`); fuera de ese rango debe lanzar `ValueError`.  
**Prueba que reproduce el error:**  
`tests/test_issue_03.py::test_issue_03_rechaza_coordenadas_fuera_de_arequipa`
