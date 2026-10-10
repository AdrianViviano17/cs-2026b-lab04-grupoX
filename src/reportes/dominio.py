from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from abc import ABC, abstractmethod


class EstadoReporte(Enum):
    BORRADOR = "BORRADOR"
    ENCOLADO = "ENCOLADO"
    RECIBIDO = "RECIBIDO"
    VERIFICADO = "VERIFICADO"
    ATENDIDO = "ATENDIDO"


@dataclass
class DetalleDanio:
    tipo_danio: str
    severidad: int

    def evaluar_severidad(self) -> int:
        return self.severidad


@dataclass
class Reporte:
    latitud: float
    longitud: float
    descripcion: str
    id: UUID = field(default_factory=uuid4)
    fecha_hora: datetime = field(default_factory=datetime.now)
    estado: EstadoReporte = EstadoReporte.BORRADOR
    detalles: List[DetalleDanio] = field(default_factory=list)

    def guardar_localmente((self) -> None:
        self.estado = EstadoReporte.ENCOLADO

    def sincronizar(self) -> None:
        self.estado = EstadoReporte.RECIBIDO

    def cambiar_estado(self, nuevo_estado: EstadoReporte) -> None:
        self.estado = nuevo_estado


class ServicioSincronizacion(ABC):
    @abstractmethod
    def enviar_reporte(self, r: Reporte) -> bool:
        pass


class SyncHttpAdapter(ServicioSincronizacion):
    def enviar_reporte(self, r: Reporte) -> bool:
        # Simulación de envío HTTP hacia el servidor central
        raise NotImplementedError("Integrar con el backend central")


class RepositorioReportes(ABC):
    @abstractmethod
    def guardar_local(self, r: Reporte) -> None:
        pass

    @abstractmethod
    def obtener_encolados(self) -> List[Reporte]:
        pass


class NotificadorBrigada(ABC):
    @abstractmethod
    def notificar_alerta(self, r: Reporte) -> None:
        pass


class GestorReportes:
    def __init__(
        self,
        repo: RepositorioReportes,
        sync_service: ServicioSincronizacion,
        notificador: NotificadorBrigada,
    ):
        self.repo = repo
        self.sync_service = sync_service
        self.notificador = notificador

    def procesar_envio_offline(self, r: Reporte) -> None:
        r.guardar_localmente()
        self.repo.guardar_local(r)

    def sincronizar_pendientes(self) -> None:
        pendientes = self.repo.obtener_encolados()
        for reporte in pendientes:
            exito = self.sync_service.enviar_reporte(reporte)
            if exito:
                reporte.cambiar_estado(EstadoReporte.RECIBIDO)
                self.repo.guardar_local(reporte)
                self.notificador.notificar_alerta(reporte)
