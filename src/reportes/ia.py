# Strategy para Proveedores de IA
class ClasificadorIA(ABC):
    @abstractmethod
    def clasificar_severidad(self, descripcion: str) -> str: pass

class ClasificadorLocal(ClasificadorIA):
    def clasificar_severidad(self, descripcion: str) -> str:
        return "ALTA" if ("derrumb" in descripcion.lower() or "atrapad" in descripcion.lower()) else "MEDIA"

# Decorator para Caché de IA
class ConCacheIA(ClasificadorIA):
    def __init__(self, interno: ClasificadorIA):
        self._interno = interno
        self._cache = {}

    def clasificar_severidad(self, descripcion: str) -> str:
        if descripcion not in self._cache:
            self._cache[descripcion] = self._interno.clasificar_severidad(descripcion)
        return self._cache[descripcion]

# Chain of Responsibility (Guardrails de Validación de Entrada/Salida)
class Guardrail(ABC):
    def __init__(self, siguiente=None):
        self._siguiente = siguiente

    def validar(self, texto: str) -> str:
        res = self._aplicar(texto)
        return self._siguiente.validar(res) if self._siguiente else res

    @abstractmethod
    def _aplicar(self, texto: str) -> str: pass

class GuardrailLongitudMinima(Guardrail):
    def _aplicar(self, texto: str) -> str:
        if not texto or len(texto.strip()) < 5:
            raise ValueError("Guardrail IA: Descripción demasiado corta para clasificar")
        return texto

class GuardrailLenguajeProhibido(Guardrail):
    PROHIBIDAS = ["broma", "fake", "falso"]
    def _aplicar(self, texto: str) -> str:
        for p in self.PROHIBIDAS:
            if p in texto.lower():
                raise ValueError(f"Guardrail IA: Contenido no permitido '{p}'")
        return texto
