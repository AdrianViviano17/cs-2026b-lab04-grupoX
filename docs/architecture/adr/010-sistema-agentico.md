# ADR-010: Arquitectura del Sistema Agéntico para Resolución de Issues en SismoReporta AQP

* **Estado:** Aceptado  
* **Fecha:** 2026-11-21  
* **Contexto:** Laboratorio 10 – Construcción de Software (Caso 8: SismoReporta AQP)[cite: 18]  

## 1. Contexto y Problema
Para automatizar la resolución de incidencias en el código fuente (`ISSUE-01`, `ISSUE-02`, `ISSUE-03`) sin comprometer la integridad de las pruebas ni exponer el repositorio a comandos arbitrarios (OWASP LLM06) o inyecciones indirectas (OWASP LLM01), se requiere una arquitectura agéntica determinista, auditable y reproducible en integración continua[cite: 8, 11, 18].

## 2. Decisión Arquitectónica
Se implementa un mini framework en Python (`agentes/agente/`) basado en los siguientes pilares:
1. **Arquetipo híbrido (Planificador-Ejecutor + ReAct):** Modelado como una **máquina de estados finitos** (`Decidiendo` $\rightarrow$ `ValidandoContrato` $\rightarrow$ `EvaluandoPolitica` $\rightarrow$ `Ejecutando` $\rightarrow$ `Observando` $\rightarrow$ `Finalizado`/`LimiteAlcanzado`)[cite: 5, 6, 10].
2. **Coordinación selectiva (Principio de parsimonia):** Agente único para incidencias localizadas (#01 y #03) y esquema multiagente **Gestor + Actor-Crítico** (máximo 2 rondas, con `revisor` de solo lectura) para cambios de alta criticidad (#02)[cite: 7, 13, 19].
3. **Herramientas acotadas y memoria externa:** Sandbox estricto en el directorio raíz, herramientas atómicas incluyendo inspección AST (`mapa_repo`) y memoria de trabajo persistente en `notas.md` (`anotar`/`leer_notas`)[cite: 12, 19].
4. **Control y Human-in-the-loop:** Validación de contrato JSON antes de actuar, lista blanca de comandos, protección de escritura sobre `tests/`, límite de 12 pasos y aprobación humana explícita (`aprobar_edicion`) antes de aplicar parches[cite: 11, 12, 13, 19].
5. **Desacoplamiento del modelo (Patrón Strategy):** Interfaz `Modelo` con implementaciones `ModeloInteractivo` (captura manual sin API key), `ModeloGrabado` (reproducción determinista en CI/CD) y adaptadores reales[cite: 10, 13].

## 3. Alternativas Descartadas
* **Flujo de trabajo fijo (Pipeline lineal):** Descartado para resolución de bugs porque la ubicación exacta del defecto y la cantidad de iteraciones de prueba varían según cada issue[cite: 3, 10].
* **Agente con acceso libre a shell (`bash` sin restricciones):** Descartado por riesgo crítico de exceso de agencia (OWASP LLM06) e inyección indirecta de comandos remotos[cite: 8, 9].
* **Coordinación democrática (3 revisores votando) para todos los issues:** Descartada por triplicar latencia y consumo de tokens en incidencias simples[cite: 7].

## 4. Consecuencias
* **Positivas:** Ejecución 100% reproducible en GitHub Actions mediante `ModeloGrabado`, trazabilidad completa en formato JSONL con generación automática de diagramas Mermaid y aislamiento efectivo frente a modificaciones indebidas en `tests/`[cite: 13, 14].
* **Negativas / Compromisos:** Requiere mantener sincronizadas las trayectorias grabadas cuando cambian los fragmentos de contexto del código fuente, y añade latencia adicional en las tareas que requieren doble ronda Actor-Crítico[cite: 7].
