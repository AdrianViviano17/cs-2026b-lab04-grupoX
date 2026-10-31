# ADR 007: Cacheo de Inferencia de Severidad por IA mediante Redis (Read-Through)

* **Estado:** Aceptado
* **Contexto:** 
  La clasificación de la severidad del reporte sísmico basada en modelos de Procesamiento de Lenguaje Natural (IA/NLP) implica un alto costo computacional. En situaciones de emergencia sísmica, miles de usuarios envían descripciones de texto redundantes (ej. *"Sismo fuerte en el centro de Arequipa"*), lo que provoca cuellos de botella e ineficiencias si se invoca el motor de inferencia por cada petición individual.
* **Decisión:** 
  Implementar una estrategia de caché de lectura (**Read-Through**) respaldada por una instancia en memoria de **Redis**, encapsulada a través de un patrón Decorador/Proxy (`ConCacheIA`) sobre la clase clasificadora. Las inferencias resultantes se almacenan utilizando un hash del texto y un tiempo de vida corto (TTL).
* **Consecuencias:** 
  * **Positivas:** Reducción sustancial del tiempo de respuesta (latencia cercana a cero en descripciones repetidas), aumento significativo del throughput del sistema y aislamiento del componente de IA ante sobrecargas.
  * **Negativas:** Introduce una nueva dependencia de infraestructura (servidor/clúster Redis) y la necesidad de gestionar políticas de expiración para evitar la retención de respuestas obsoletas.
