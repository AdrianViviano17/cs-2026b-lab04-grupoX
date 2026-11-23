# Delegación Progresiva y Humano en el Circuito - SismoReporta AQP (Lab 10)

## 1. Control Activo Actual (`aprobar_edicion` en `Politica`)
En el mini framework implementado (`agentes/agente/politica.py` y `agentes/orquestador.py`), el agente opera actualmente bajo el patrón **Human-in-the-loop (Aprobar o rechazar)**:
* Antes de ejecutar `editar_archivo`, la política invoca `aprobar_edicion(args)` solicitando confirmación explícita por consola (`s` o `n`) y rechazando cualquier entrada ambigua[cite: 8, 13, 19].
* La carpeta `tests/` permanece protegida contra escritura y ningún agente tiene permisos de `git push` o fusión de Pull Requests[cite: 12, 13, 17].

## 2. Hoja de Ruta de Evolución del Rol Humano (Albada, 2025, cap. 13)

| Etapa / Rol Humano | Permisos otorgados al agente en SismoReporta AQP | Evidencia en trazas JSONL requerida para avanzar a la siguiente etapa |
| :--- | :--- | :--- |
| **1. Ejecutor** *(Supervisión paso a paso)* | Solo lectura (`listar_archivos`, `leer_archivo`, `buscar`, `mapa_repo`) y diagnóstico de issues. El humano redacta y aplica el parche manualmente[cite: 8]. | El agente localiza correctamente la función defectuosa en `src/` en $\le 4$ pasos sin alucinar rutas en 10 issues consecutivos. |
| **2. Revisor** *(Estado actual del proyecto)* | Lectura + edición supervisada (`editar_archivo` requiere aprobación `s`/`n` humana) + ejecución de `pytest` y `radon` en rama aislada. El humano revisa y aprueba el Pull Request[cite: 8, 17, 19]. | $\ge 20$ issues resueltos con **0 violaciones de contrato**, **0 intentos bloqueados por política** (ej. comandos externos o edición en `tests/`) y $\ge 95\%$ de parches aprobados sin retrabajo. |
| **3. Colaborador** *(Autonomía en rama de desarrollo)* | Edición automática dentro de `src/` sin interrupción por cada archivo (`aprobar_edicion=None`), respaldada por bucle multiagente **Actor-Crítico** obligatorio y revisión humana únicamente al final en el Pull Request[cite: 8, 17]. | $\ge 50$ PRs fusionados en producción sin regresiones ni incidencias de seguridad (OWASP LLM01 / LLM06) detectadas en auditorías posteriores. |
| **4. Gobernador** *(Auditoría por políticas y métricas)* | Creación autónoma de ramas, ejecución de suites completas de CI/CD y apertura de PRs listos para fusión automática si cumplen umbrales de cobertura y complejidad ciclomática (`radon cc` grado A/B); el humano define políticas y audita trazas[cite: 8, 12]. | Cumplimiento sostenido de SLAs de calidad, trazabilidad completa en JSONL y cero incidentes críticos durante un ciclo completo de despliegue. |
