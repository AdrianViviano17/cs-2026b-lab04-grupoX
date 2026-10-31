import random
import heapq
import statistics

def simular_ingesta(lam: float, workers: int, tiempo_servicio_fn, segundos: float = 120.0, semilla: int = 42):
    rnd = random.Random(semilla)
    t, llegadas = 0.0, []
    while t < segundos:
        t += rnd.expovariate(lam)
        llegadas.append(t)

    libres = [0.0] * workers
    heapq.heapify(libres)
    respuestas = []

    for a in llegadas:
        libre = heapq.heappop(libres)
        inicio = max(a, libre)
        fin = inicio + tiempo_servicio_fn(rnd)
        heapq.heappush(libres, fin)
        respuestas.append((fin - a) * 1000)  # Convertir a ms

    respuestas.sort()
    p95_idx = int(0.95 * (len(respuestas) - 1))
    return {
        "total": len(respuestas),
        "p50": respuestas[int(0.50 * len(respuestas))],
        "p95": respuestas[p95_idx],
        "promedio": statistics.mean(respuestas)
    }

# Perfiles de tiempo de servicio según tácticas aplicadas (en segundos)
def servicio_sin_tacticas(rnd):
    return rnd.lognormvariate(0.5, 0.4)  # ~1.8 segundos por reporte sin índices

def servicio_con_indice_postgis(rnd):
    return rnd.lognormvariate(-1.8, 0.2)  # ~0.17 segundos con índice espacial

if __name__ == "__main__":
    # Ingesta durante simulacro (aprox. 12 solicitudes por segundo sostenidas)
    res_base = simular_ingesta(lam=12, workers=4, tiempo_servicio_fn=servicio_sin_tacticas)
    res_opt = simular_ingesta(lam=12, workers=4, tiempo_servicio_fn=servicio_con_indice_postgis)

    print(f"Sin tácticas -> p95: {res_base['p95']:.2f} ms")
    print(f"Con Índice PostGIS -> p95: {res_opt['p95']:.2f} ms")
