workspace "SismoReporta AQP" "Modelo C4 del Sistema Offline-First de Reporte Sísmico para Arequipa" {

    !identifiers hierarchical

    model {
        # --- PERSONAS (Nivel 1) ---
        ciudadano = person "Ciudadano" "Persona afectada por un sismo que registra reportes de daños."
        brigadista = person "Brigadista / Coordinador" "Personal de Defensa Civil que gestiona la emergencia y asigna recursos."

        # --- SISTEMA PRINCIPAL ---
        sismoReporta = softwareSystem "SismoReporta AQP" "Permite registrar reportes sísmicos offline y gestionar la atención de emergencias." {
            
            # (En el Paso 2 agregaremos los contenedores dentro de este bloque)
        }

        # --- SISTEMAS EXTERNOS (Nivel 1) ---
        mapas = softwareSystem "Servicio de Mapas" "Provee mapas tiles e imágenes satelitales (OpenStreetMap/Mapbox)." "Externo"
        s3 = softwareSystem "Almacenamiento de Fotos" "Almacena imágenes de evidencia de daños en la nube (AWS S3)." "Externo"
        sms = softwareSystem "Servicio de SMS" "Envía alertas críticas de emergencia por mensajería SMS." "Externo"

        # --- RELACIONES DE CONTEXTO (Nivel 1) ---
        ciudadano -> sismoReporta "Registra reportes de daños y consulta estado"
        brigadista -> sismoReporta "Visualiza mapa de calor y asigna brigadas"
        sismoReporta -> mapas "Consulta mapas tiles" "HTTPS/REST"
        sismoReporta -> s3 "Almacena fotos de evidencia" "HTTPS/API"
        sismoReporta -> sms "Envía notificaciones de emergencia" "HTTPS/REST"
    }

    views {
        systemContext sismoReporta "Contexto" "Nivel 1: Diagrama de Contexto del Sistema SismoReporta AQP" {
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
        }
    }
}
