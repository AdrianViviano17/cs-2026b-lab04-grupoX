# ADR-002: Estrategia de Almacenamiento Local Offline-First para la App Móvil/PWA

- **Estado**: Aceptado
- **Fecha**: 2026-09-30
- **Decisores**: Equipo de Desarrollo

## Contexto
Durante un sismo, la infraestructura de telecomunicaciones suele colapsar (QA-01). Los ciudadanos deben poder generar reportes con fotos y geolocalización aún sin señal.

## Alternativas Consideradas
1. **App Web Tradicional**: Requiere conexión obligatoria para enviar formularios.
2. **Arquitectura Offline-First con IndexedDB / SQLite local + Background Sync**: Guarda reportes localmente y se sincroniza en segundo plano al detectar red.

## Decisión
Elegimos la **Arquitectura Offline-First**. Se implementará Service Workers con IndexedDB en PWA (o SQLite en Flutter), registrando coordenadas y fotos con marcas de tiempo locales.

## Consecuencias
* **Positivas**: Cero pérdida de reportes por falta de señal en la zona del desastre.
* **Negativas / Riesgos**: Riesgo de reportes duplicados si la sincronización falla a mitad de transmisión; requiere un mecanismo de deduplicación en el backend.
