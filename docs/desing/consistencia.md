# Auditoría de Consistencia (Reglas C1 - C5)

| Regla | Hallazgo Reportado por IA | Verificación del Equipo Humano | Decisión / Estado |
| :--- | :--- | :--- | :--- |
| **C1** | `N.notificarAlerta(reporte)` en secuencia violaba C1 por no existir la clase. | **Falso Positivo**: `NotificadorBrigada` está definida como una interfaz (`<<puerto>>`) válida. | Hallazgo Rechazado. |
| **C2** | La transición "Productor/Coordinador asigna" no tenía método explícito. | **Hallazgo Correcto**: Faltaba la operación de cambio de estado. | Corregido: Se añadió el método `asignarBrigada()` en la clase `Reporte`. |
| **C4** | La IA reportó una dependencia circular entre `sincronizacion` y `brigadas`. | **Falso Positivo**: La IA interpretó al revés la dirección de la flecha de dependencia. | Hallazgo Rechazado. |
| **C5** | Inconsistencia en la enumeración de estados. | **Hallazgo Correcto**: Se mezclaba `EN_COLADO` con `ENCOLADO`. | Corregido: Unificado a `ENCOLADO` en todos los archivos de diseño y código. |
