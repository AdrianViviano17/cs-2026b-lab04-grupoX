# Drivers Arquitectónicos - SismoReporta AQP

## 1. Requisitos Funcionales Clave
| ID | Requisito | Actor | Prioridad |
|---|---|---|---|
| RF-01 | Registrar reporte de daños con foto, descripción y ubicación GPS (sincronización offline) | Ciudadano | Alta |
| RF-02 | Visualizar mapa interactivo de daños con zonas de severidad y filtrado | Brigadista / Coordinador / Ciudadano | Alta |
| RF-03 | Priorización automática de zonas críticas según algoritmo de severidad | Coordinador | Alta |
| RF-04 | Asignación y seguimiento en tiempo real de brigadas a zonas de atención | Coordinador / Brigadista | Media |
| RF-05 | Envío de alertas masivas e instrucciones de emergencia a la población | Coordinador | Media |

## 2. Atributos de Calidad (Ordenados por Prioridad)
1. **Disponibilidad y Resiliencia**: El sistema debe operar en escenarios de desastre con alta saturación de red y picos masivos de uso inicial.
2. **Capacidad de Interacción (Usabilidad/Offline-first)**: La app debe guardar datos localmente si no hay conexión y enviarlos automáticamente al recuperar señal.
3. **Desempeño / Rendimiento**: La ingesta masiva de reportes no debe colapsar la base de datos principal.
4. **Modificabilidad**: Capacidad de agregar nuevos conectores de alertas (SMS, WhatsApp, radio) sin modificar el núcleo del sistema.

## 3. Restricciones
| ID | Tipo | Restricción |
|---|---|---|
| R-01 | Plazo | MVP funcional en producción en 1 mes. |
| R-02 | Equipo | Máximo 3 desarrolladores con dominio de Python, Node.js y React/Flutter. |
| R-03 | Presupuesto | Hosting de bajo costo (VPS único o servicios Serverless de capa gratuita). |
| R-04 | Normativa | Cumplimiento de la Ley N.º 29733 (Protección de Datos Personales en Perú) para la gestión de ubicaciones. |

## 4. Escenarios de Atributos de Calidad

| ID | Atributo | Fuente | Estímulo | Entorno | Artefacto | Respuesta | Medida |
|---|---|---|---|---|---|---|---|
| QA-01 | Disponibilidad | 20,000 Ciudadanos | Envían reportes simultáneos en la 1ª hora tras el sismo | Red móvil 3G/4G congestionada | PWA / App Móvil y Cola de Ingesta | El reporte se guarda localmente en SQLite/IndexedDB y se sincroniza al recuperar red | 0% reportes perdidos; recepción exitosa en backend en p95 ≤ 5 s al reconectar. |
| QA-02 | Rendimiento | 50 Brigadistas / Coordinadores | Consultan y filtran el mapa de daños en tiempo real | Hora pico del desastre | Módulo de Mapas y Base de Datos espacial | Devuelve las capas geográficas optimizadas (MVT/GeoJSON simplificado) | Tiempo de respuesta p95 ≤ 2.5 s para renderizado de mapa. |
| QA-03 | Modificabilidad| Equipo de Desarrollo | Solicitan integrar un nuevo canal de notificación masiva (ej. Telegram) | Mantenimiento / Desarrollo | Módulo de Notificaciones | Se agrega el conector mediante interfaz/adaptador sin alterar la lógica de negocio | Esfuerzo ≤ 2 días-persona. |
