class EstadoReporte(ABC):
    nombre = "?"
    def recibir(self, reporte): raise ValueError(f"No se puede recibir un reporte en estado {self.nombre}")
    def verificar(self, reporte, op_id): raise ValueError(f"No se puede verificar un reporte en estado {self.nombre}")
    def atender(self, reporte): raise ValueError(f"No se puede atender un reporte en estado {self.nombre}")

class Borrador(EstadoReporte):
    nombre = "BORRADOR"
    def recibir(self, reporte): reporte.cambiar_estado(Recibido())

class Encolado(EstadoReporte):
    nombre = "ENCOLADO"
    def recibir(self, reporte): reporte.cambiar_estado(Recibido())

class Recibido(EstadoReporte):
    nombre = "RECIBIDO"
    def verificar(self, reporte, op_id):
        reporte.operacion_id = op_id
        reporte.cambiar_estado(Verificado())

class Verificado(EstadoReporte):
    nombre = "VERIFICADO"
    def atender(self, reporte): reporte.cambiar_estado(Atendido())

class Atendido(EstadoReporte):
    nombre = "ATENDIDO"
