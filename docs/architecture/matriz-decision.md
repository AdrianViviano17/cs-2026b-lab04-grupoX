# Matriz de Decisión Arquitectónica - SismoReporta AQP

## Alternativas Consideradas
* **A. Monolito Tradicional en Capas**: Presentación, Lógica y Datos en una sola aplicación relacional.
* **B. Arquitectura Orientada a Eventos con Microservicios**: Ingesta mediante colas (Kafka/RabbitMQ), microservicios independientes y base de datos distribuida.
* **C. Monolito Modular con Ingesta Asíncrona (PWA + CQRS básico + Colas)**: Un solo despliegue estructurado por módulos de dominio, con cola Redis/Celery para procesar reportes en segundo plano.

## Criterios y Pesos (Suma = 100%)
| Criterio | Peso | Justificación |
|---|---|---|
| Tiempo de entrega | 25% | R-01: El MVP debe entregarse en 1 mes. |
| Disponibilidad en picos | 25% | QA-01: Soporte de 20,000 reportes sin pérdida de datos. |
| Simplicidad operativa | 20% | R-02: Equipo pequeño de 3 personas sin DevOps dedicado. |
| Costo operativo | 15% | R-03: Presupuesto reducido (VPS/recursos limitados). |
| Modificabilidad | 15% | QA-03: Capacidad de añadir adaptadores de notificación. |

## Matriz de Evaluación (Puntaje 1: Muy malo, 5: Excelente)

| Criterio (Peso) | A. Monolito Capas | B. Microservicios | C. Monolito Modular Asíncrono |
|---|---|---|---|
| Tiempo de entrega (25%) | 5 | 2 | 4 |
| Disponibilidad en picos (25%) | 2 | 5 | 4 |
| Simplicidad operativa (20%) | 5 | 1 | 4 |
| Costo operativo (15%) | 5 | 2 | 4 |
| Modificabilidad (15%) | 2 | 5 | 4 |
| **Total Ponderado** | **3.80** | **2.80** | **4.00** |

*Cálculos:*
* **A:** (5*0.25) + (2*0.25) + (5*0.20) + (5*0.15) + (2*0.15) = 1.25 + 0.50 + 1.00 + 0.75 + 0.30 = **3.80**
* **B:** (2*0.25) + (5*0.25) + (1*0.20) + (2*0.15) + (5*0.15) = 0.50 + 1.25 + 0.20 + 0.30 + 0.75 = **2.80**
* **C:** (4*0.25) + (4*0.25) + (4*0.20) + (4*0.15) + (4*0.15) = 1.00 + 1.00 + 0.80 + 0.60 + 0.60 = **4.00**

## Conclusión
Se selecciona la **Alternativa C: Monolito Modular con Ingesta Asíncrona**. Ofrece el mejor equilibrio para absorber picos extremos de tráfico mediante colas asíncronas sin incurrir en la sobrecarga operativa de microservicios. Ver [ADR-001](adr/001-estilo-arquitectonico.md).
