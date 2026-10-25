# Inventario de Elementos de Arquitectura - SismoReporta AQP

| Elemento | Tipo C4 | Descripción / Responsabilidad | Origen (Lab 04 / Lab 05) |
| :--- | :--- | :--- | :--- |
| **Ciudadano** | Persona | Usuario afectado que reporta sismos y daños, con o sin conectividad. | `drivers.md` (Lab 04) |
| **Brigadista / Coordinador** | Persona | Personal de Defensa Civil que evalúa reportes y asigna brigadas de atención. | `drivers.md` (Lab 04) |
| **SismoReporta AQP** | Sistema de Software | Sistema principal offline-first de registro, geolocalización y gestión de emergencias sísmicas. | Caso de Uso General |
| **Servicio de Mapas (OpenStreetMap/Mapbox)** | Sistema Externo | Provee capas de mapas tiles e imágenes satelitales. | `ADR-001` (Lab 04) |
| **Almacenamiento de Fotos (AWS S3)** | Sistema Externo | Almacena las evidencias fotográficas de los reportes. | `ADR-001` (Lab 04) |
| **Servicio de SMS (Twilio)** | Sistema Externo | Envía alertas críticas por mensajería SMS en zonas sin datos. | `drivers.md` (Lab 04) |
| **App PWA Offline** | Contenedor | Aplicación web progresiva cliente en el dispositivo del usuario con almacenamiento local (IndexedDB). | `ADR-001` (Lab 04) |
| **API SismoReporta** | Contenedor | Monolito modular que procesa la ingesta de reportes, mapas y gestión de brigadas. | `ADR-001` (Lab 04) |
| **Cola de Mensajes** | Contenedor | Cola para el procesamiento asíncrono y desacoplado de reportes e imágenes. | `ADR-001` (Lab 04) |
| **Base de Datos Geoespacial** | Contenedor | Almacena reportes, estados, usuarios y geometrías GIS. | `ADR-001` (Lab 04) |
| **Módulo Ingesta** | Componente | Procesa los reportes de emergencias y valida consistencia. | `paquetes.puml` (Lab 05) |
| **Módulo GIS / Mapa** | Componente | Genera mapas de calor y maneja coordenadas. | `paquetes.puml` (Lab 05) |
| **Módulo Brigadas** | Componente | Gestiona la asignación y estado de atención de brigadas. | `paquetes.puml` (Lab 05) |
| **Módulo Infraestructura** | Componente | Conecta con adaptadores de BD, colas y servicios externos. | `paquetes.puml` (Lab 05) |
| **Sincronizar Reporte Offline** | Flujo Dinámico | Secuencia de sincronización cuando se detecta reconexión a Internet. | `secuencia-sincronizar-reporte.puml` (Lab 05) |
