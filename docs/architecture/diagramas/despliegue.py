from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.generic.device import Mobile
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import Django
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Celery
from diagrams.onprem.network import Internet

graph_attr = {"fontsize": "18", "bgcolor": "white", "pad": "0.5"}

with Diagram("SismoReporta AQP - Vista de Despliegue", filename="despliegue", show=False, direction="LR", graph_attr=graph_attr):
    
    ciudadanos = Users("Ciudadanos y Brigadistas")
    app_movil = Mobile("App Móvil / PWA\n(Offline-First)")

    with Cluster("Servidor VPS Nube (Único Despliegue)"):
        proxy = Nginx("Nginx\n(Reverse Proxy HTTPS)")
        
        with Cluster("Monolito Modular Backend"):
            app = Django("Django / FastAPI\n(API & Módulos)")
            worker = Celery("Workers Ingesta")
        
        cache = Redis("Redis\n(Colas + Caché)")
        db = PostgreSQL("PostgreSQL + PostGIS\n(Base Datos Espacial)")

    sms_gateway = Internet("Servicio Externo\nSMS / WhatsApp API")

    ciudadanos >> app_movil >> Edge(label="Sync HTTPS") >> proxy >> app
    app >> Edge(label="Encola reportes") >> cache >> worker
    worker >> Edge(label="Guarda reporte procesado") >> db
    app >> Edge(label="Consultas GIS") >> db
    worker >> Edge(label="Alertas masivas", style="dashed") >> sms_gateway
