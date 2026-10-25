# ADR-004: Adopción del Modelo C4 para la Visualización y Documentación de Arquitectura

**Estado:** Aceptado  
**Fecha:** 17 de Octubre de 2026  
**Autores:** Equipo de Desarrollo SismoReporta AQP  

---

## 1. Contexto y Problema
En los laboratorios anteriores (Lab 04 y Lab 05) se definieron los requerimientos del sistema, la elección de la arquitectura monolítica modular (ADR-001) y el diseño detallado en UML. Sin embargo, la comunicación visual de la arquitectura presentaba los siguientes inconvenientes:

1. **Ambigüedad de diagramas tradicionales:** Los diagramas de "cajas y flechas" previos no diferenciaban claramente entre fronteras del sistema, aplicaciones ejecutables (contenedores C4) y módulos internos de código.
2. **Inconsistencia entre vistas:** Al modificar un elemento en la arquitectura, existía el riesgo de desalineación entre la documentación técnica, los esquemas UML y las vistas de despliegue.
3. **Múltiples audiencias:** Se requería explicar el sistema tanto a autoridades municipales y coordinadores de Defensa Civil (público no técnico) como a desarrolladores e ingenieros DevOps (público técnico).

---

## 2. Decisión
Se decide adoptar el **Modelo C4 (Simon Brown)** como estándar de documentación arquitectónica mediante el enfoque de **"Arquitectura como Código" (Architecture as Code)** utilizando **Structurizr DSL** (`workspace.dsl`) como modelo único fuente de verdad.

A partir de este modelo único se derivan las siguientes vistas:
1. **Nivel 1 (Contexto del Sistema):** Representa a los usuarios (Ciudadanos, Brigadistas) y los servicios externos (Mapas tiles, AWS S3, Twilio SMS).
2. **Nivel 2 (Contenedores):** Define los entornos ejecutables y almacenes de datos: App PWA Offline (React), API SismoReporta (FastAPI), Cola de Mensajes (Redis) y Base de Datos Geoespacial (PostgreSQL/PostGIS).
3. **Nivel 3 (Componentes):** Desglosa la API principal en sus módulos internos (Ingesta, GIS/Mapa, Brigadas e Infraestructura), en estricta coherencia con el diagrama de paquetes UML del Lab 05.
4. **Vista Dinámica:** Detalla la secuencia de pasos numerados del flujo crítico de *Sincronización Offline*.
5. **Vista de Despliegue:** Muestra el mapeo de los contenedores dentro de un VPS con Docker Compose y los dispositivos móviles de los usuarios.

---

## 3. Consecuencias

### Positivas (+)
* **Fuente Única de Verdad:** Cualquier cambio en un contenedor o protocolo dentro de `workspace.dsl` actualiza de forma consistente e instantánea las 5 vistas del sistema.
* **Trazabilidad Garantizada:** Mantiene alineación directa con los drivers de calidad (Lab 04) y los diagramas de clases y paquetes (Lab 05).
* **Comunicación Multinivel:** Facilita la explicación del sistema a perfiles ejecutivos (Nivel 1) e ingenieros de software (Niveles 2 y 3).

### Negativas (-)
* **Curva de Aprendizaje:** El equipo debió aprender la sintaxis de Structurizr DSL y el uso de la CLI/Docker de Structurizr para la exportación de diagramas.
* **Herramientas Experimentales:** El soporte de renderizado de diagramas C4 en Mermaid para el `README.md` de GitHub requiere configuraciones específicas.
