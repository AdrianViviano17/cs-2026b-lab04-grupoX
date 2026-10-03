# SismoReporta AQP - Laboratorio 04: Fundamentos de Arquitectura de Software

**Asignatura**: Construcción de Software (2026-B)  
**Escuela Profesional de Ingeniería de Sistemas - UNSA**

## Integrantes (Grupo XX)
| Nombre | Rol en el laboratorio |
|---|---|
| [Adrian Viviano] | Diagramador (Mermaid / PlantUML) |
| [Adrian Viviano] | Redactor de ADRs y drivers |
| [Adrian Viviano] | Verificador de IA y Script Python Diagrams |

## Caso Elegido: SismoReporta AQP
Plataforma de reporte ciudadano de daños tras un sismo en Arequipa para apoyar a Defensa Civil y brigadistas. Permite registrar reportes con foto y ubicación incluso sin señal de internet, visualizándolos en un mapa de calor priorizado por severidad.
* **Atributo Crítico**: Disponibilidad y resiliencia (20,000 reportes en la primera hora tras el sismo con red móvil congestionada; sincronización offline).

## Arquitectura Elegida
```mermaid
flowchart TB
    CIU["Ciudadano (PWA Offline)"]
    BRI["Brigadista / Coordinador"]

    subgraph APP ["SismoReporta AQP (Monolito Modular)"]
        API["API REST"]
        M1["Módulo Ingesta"]
        M2["Módulo GIS / Mapa"]
        M3["Módulo Brigadas"]
        INF["Infraestructura"]
    end

    QUEUE[("Cola Redis")]
    DB[("PostgreSQL + PostGIS")]

    CIU --> API --> M1 & M2 & M3 --> INF
    M1 --> QUEUE --> INF
    INF --> DB
