workspace "SismoReporta AQP" "Modelo C4 del Sistema Offline-First de Reporte Sísmico para Arequipa" {

    !identifiers hierarchical

    model {
        # --- PERSONAS (Nivel 1) ---
        ciudadano = person "Ciudadano" "Persona afectada por un sismo que registra reportes de daños."
        brigadista = person "Brigadista / Coordinador" "Personal de Defensa Civil que gestiona la emergencia y asigna recursos."

        # --- SISTEMA PRINCIPAL Y CONTENEDORES (Nivel 2) ---
        sismoReporta = softwareSystem "SismoReporta AQP" "Permite registrar reportes sísmicos offline y gestionar la atención de emergencias." {
            
            pwa = container "Aplicación Web Progresiva" "Interfaz cliente offline-first para ciudadanos y brigadistas." "React + PWA / Service Worker + IndexedDB" "Web Browser"
            
            # --- COMPONENTES (Nivel 3) ---
            api = container "API SismoReporta" "Monolito modular que procesa la ingesta de reportes, mapas y gestión de brigadas." "Python / FastAPI" {
                
                ingesta = component "Módulo Ingesta" "Recibe, valida y gestiona la persistencia de reportes de daños." "FastAPI Router / Python"
                gis = component "Módulo GIS / Mapa" "Procesa coordenadas geoespaciales y calcula mapas de calor." "GeoPandas / Python"
                brigadas = component "Módulo Brigadas" "Gestiona asignación, rutas y estados de atención de brigadas." "FastAPI Router / Python"
                infraestructura = component "Módulo Infraestructura" "Conecta con adaptadores de BD, colas y servicios externos." "SQLAlchemy / Redis SDK"
            }
            
            cola = container "Cola de Mensajes" "Gestiona la cola de tareas asíncronas para procesamiento de imágenes y alertas." "Redis" "Queue"
            
            db = container "Base de Datos Geoespacial" "Almacena usuarios, reportes de daños, estados y geometrías GIS." "PostgreSQL 16 + PostGIS" "Database"
        }

        # --- SISTEMAS EXTERNOS (Nivel 1) ---
        mapas = softwareSystem "Servicio de Mapas" "Provee mapas tiles e imágenes satelitales (OpenStreetMap/Mapbox)." "Externo"
        s3 = softwareSystem "Almacenamiento de Fotos" "Almacena imágenes de evidencia de daños en la nube (AWS S3)." "Externo"
        sms = softwareSystem "Servicio de SMS" "Envía alertas críticas de emergencia por mensajería SMS." "Externo"

        # --- RELACIONES DE CONTEXTO Y CONTENEDORES (Niveles 1 y 2) ---
        ciudadano -> sismoReporta "Registra reportes de daños y consulta estado"
        brigadista -> sismoReporta "Visualiza mapa de calor y asigna brigadas"
        sismoReporta -> mapas "Consulta mapas tiles" "HTTPS/REST"
        sismoReporta -> s3 "Almacena fotos de evidencia" "HTTPS/API"
        sismoReporta -> sms "Envía notificaciones de emergencia" "HTTPS/REST"

        ciudadano -> sismoReporta.pwa "Usa para reportar emergencias offline" "HTTPS"
        brigadista -> sismoReporta.pwa "Usa para gestionar mapa de calor y brigadas" "HTTPS"
        
        sismoReporta.pwa -> sismoReporta.api "Sincroniza reportes encolados y consume API" "HTTPS/JSON REST"
        sismoReporta.pwa -> mapas "Descarga mapas tiles en caché" "HTTPS"
        
        sismoReporta.api -> sismoReporta.db "Lee y escribe reportes y datos GIS" "SQL/TCP"
        sismoReporta.api -> sismoReporta.cola "Encola tareas de procesamiento asíncrono" "Redis protocol"
        sismoReporta.api -> s3 "Sube fotos de evidencia de daños" "HTTPS/AWS SDK"
        sismoReporta.api -> sms "Solicita envío de SMS de emergencia" "HTTPS/REST"

        # --- RELACIONES DE COMPONENTES (Nivel 3) ---
        sismoReporta.pwa -> sismoReporta.api.ingesta "Envía reporte sísmico" "HTTPS/JSON"
        sismoReporta.pwa -> sismoReporta.api.gis "Consulta mapas de calor" "HTTPS/JSON"
        sismoReporta.pwa -> sismoReporta.api.brigadas "Asigna y actualiza brigadas" "HTTPS/JSON"
        
        sismoReporta.api.ingesta -> sismoReporta.api.gis "Notifica nuevos puntos geoespaciales"
        sismoReporta.api.ingesta -> sismoReporta.api.infraestructura "Persiste reporte y encola tareas"
        sismoReporta.api.brigadas -> sismoReporta.api.gis "Consulta concentración de emergencias"
        sismoReporta.api.brigadas -> sismoReporta.api.infraestructura "Notifica asignación por SMS"
        sismoReporta.api.gis -> sismoReporta.api.infraestructura "Consulta geometrías y capas GIS"
        
        sismoReporta.api.infraestructura -> sismoReporta.db "Lee/Escribe SQL" "SQL/TCP"
        sismoReporta.api.infraestructura -> sismoReporta.cola "Encola mensajes" "Redis protocol"
        sismoReporta.api.infraestructura -> s3 "Sube archivos" "HTTPS"
        sismoReporta.api.infraestructura -> sms "Despacha alertas" "HTTPS"
    }

    views {
        systemContext sismoReporta "Contexto" "Nivel 1: Diagrama de Contexto del Sistema SismoReporta AQP" {
            include *
            autolayout lr
        }

        container sismoReporta "Contenedores" "Nivel 2: Diagrama de Contenedores de SismoReporta AQP" {
            include *
            autolayout lr
        }

        component sismoReporta.api "Componentes" "Nivel 3: Diagrama de Componentes de la API SismoReporta" {
            include *
            autolayout lr
        }

        styles {
            element "Person" {
                shape person
                background #08427B
                color #ffffff
            }
            element "Software System" {
                background #1168BD
                color #ffffff
            }
            element "Externo" {
                background #999999
                color #ffffff
            }
            element "Container" {
                background #438DD5
                color #ffffff
            }
            element "Component" {
                background #85BBF0
                color #000000
            }
            element "Database" {
                shape cylinder
            }
            element "Queue" {
                shape pipe
            }
            element "Web Browser" {
                shape WebBrowser
            }
        }
    }
}
