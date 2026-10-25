class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, evento: str, datos: dict): pass

class PublicadorEventos:
    def __init__(self):
        self._suscriptores = {}

    def suscribir(self, evento: str, suscriptor: Suscriptor):
        self._suscriptores.setdefault(evento, []).append(suscriptor)

    def publicar(self, evento: str, datos: dict):
        for s in self._suscriptores.get(evento, []):
            s.actualizar(evento, datos)

class NotificadorBrigadas(Suscriptor):
    def __init__(self, lista_eventos): self.eventos = lista_eventos
    def actualizar(self, evento: str, datos: dict):
        self.eventos.append(f"brigada_sms: {datos['phone']} -> Severidad {datos['severidad']}")

class ActualizadorTablero(Suscriptor):
    def __init__(self, lista_eventos): self.eventos = lista_eventos
    def actualizar(self, evento: str, datos: dict):
        self.eventos.append(f"tablero_defensa_civil: Reporte {datos['id']} VERIFICADO")
