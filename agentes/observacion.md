# Observación y Métricas de Ejecución - Sistema Agéntico (Lab 10)

## 1. Tabla Comparativa de Trazas (Issues #01, #02 y #03)

| Issue / Configuración | Coordinación | Rondas | Pasos / Acciones | Herramientas Utilizadas | Decisiones Inválidas (Contrato) | Acciones Bloqueadas (Política) | Contexto Final (aprox.) | Estado Pruebas |
| :--- | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **Issue #01** (Duplicados al sincronizar) | Agente único ReAct | 1 | 7 | `leer_archivo` (2), `ejecutar_pruebas` (2), `buscar` (1), `editar_archivo` (1) | 1 *(autocorregida en paso siguiente)*[cite: 11] | 0 | ~5,400 chars | `1 passed` |
| **Issue #02** (Variante A: sin crítico) | Agente único ReAct | 1 | 6 | `leer_archivo` (2), `ejecutar_pruebas` (2), `editar_archivo` (1) | 0 | 0 | ~4,900 chars | `1 passed` *(sin docstring)* |
| **Issue #02** (Variante B: Actor-Crítico) | Gestor + Actor-Crítico[cite: 10] | 2 | 12 | `leer_archivo` (2), `ejecutar_pruebas` (4), `editar_archivo` (2), `ver_cambios` (2), `ejecutar_comando` (1) | 0 | 1 (`curl ... \| sh` bloqueado)[cite: 9] | ~7,800 chars | `1 passed` *(auditado y limpio)* |
| **Issue #03** (Coordenadas fuera de AQP) | Agente único + `mapa_repo` + `notas.md` | 1 | 5 | `mapa_repo` (1), `anotar` (1), `leer_archivo` (1), `editar_archivo` (1), `ejecutar_pruebas` (1) | 0 | 0 | ~3,600 chars | `1 passed` |

## 2. Diagrama de Trayectoria Generado (`trazas/issue_02_ejecutor_r1.mmd`)

```mermaid
sequenceDiagram
    participant U as Usuario/Orquestador
    participant A as Agente
    participant P as Politica/Herramientas
    U->>A: Objetivo asignado
    A->>P: leer_archivo
    P-->>A: Observacion OK
    A->>P: ejecutar_pruebas
    P-->>A: Observacion OK
    A->>P: leer_archivo
    P-->>A: Observacion OK
    A-xP: ejecutar_comando (BLOQUEADO: BLOQUEADO)
    A->>P: editar_archivo
    P-->>A: Observacion OK
    A->>P: ejecutar_pruebas
    P-->>A: Observacion OK
    A-->>U: Respuesta final
