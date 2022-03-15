# Transparencia de datos
* **Definición**: Evita el problema del formato de representación de datos. Todos los nodos del sistema se entienden unos a otros. Hay 3 alternativas en el **acuerdo** a tomar para intercambiar datos:
  1. ***Mecanismo de representación de los datos independiente de la plataforma***. Los datos se convierten a un **formato genérico**.
     * *Marshalling*. Emisor convierte los datos al formato común.  
     * *Unmarshalling*. Receptor convierte los datos al formato local.  
  2. Si la ***arquitectura es común***, se negocia antes de la transmisión si se va a hacer la conversión.
  3. Transmisión de los ***datos en su formato nativo***, indicando con un **identificador** el formato de la arquitectura. 

# CORBA
* **Funcionalidad**: Permite la interoperabilidad entre sistemas heterogéneos (unos usan C, otros python...).
* **Objeto Corba**: Es un objeto **virtual** que se define mediante un **IDL (Interface Description Language)**. Se identifica de manera única mediante su referencia a objeto remoto.
* **Comunicación**: Síncrona, asíncrona y sin respuesta (one way).

# OBJECT MANAGEMENT ARCHITECTURE (OMA)
* **Object Request Broker, ORB**: Bus de comunicación entre objetos. Permite llamadas *estáticas* y *dinámicas* de objetos.
* **Common Object Services**: Compenentes que implementan servicios al nivel del sistema.
* **Domain Interfaces**: Conjunto de servicios, específicos para área de aplicaciones.
* **Application Interfaces**: Interfaces específicas de aplicaciones.

# Enterprise Service Bus, ESB
* **Definición**: Es una arquitectura software la cuál extiende el concepto de broker de mensajes a modelos sin relación Publicador-Suscriptor. Normalmente se implementa mediante **colas de mensajes**.
* **Objetivo**: ***Integrar servicios y clientes*** en sistemas heterogéneos reduciendo acoplamiento.
* **Aplicación principal**: Es el núcleo base para ***SOA (Services Oriented Architecture)***.
* **Organización**: Se organiza en 3 niveles:
  * *Conexión*. Aporta "conectividad universal" mediante APIs, protocolos y adaptadores.
  * *Comunicaciones*: Aporta interconexión entre todos los servicios conectados a él.
  * *Mediación*: Transformación semántica de los mensajes conforme sea necesario entre los extremos de la comunicación.
* **Ventajas**: 
  * Adaptación rápida. 
  * Flexibilidad.
  * Basado en estándares. 
  * Convierte tareas de programación en configuración.
* **Desventajas**: 
  * Posible punto único de fallo. 
  * Facil saturación. 
  * Requiere más sistemas para soportar el propio ESB.

# EXAMEN - Ejercicio "Solución más apropiada"
* **Acoplamiento temporal**:
  * *Acopladas en el tiempo (servidor y cliente conectados a la vez) - Síncrono*: 
    * **Comunicación no orientada a conexión UDP**.
    * **CORBA**.
    * **SOAP**.
  * *No acopladas en el tiempo - Asíncrono*:
    * **Cola de mensajes**.
* **Clientes**:
  * *Heterogéneos*:
    * **CORBA**.
    * **Cola de mensajes**.
  * *Homogéneos*:
* **Bloqueos del cliente a la espera de respuesta**:
  * *Hay bloqueo*: 
    * **Comunicación no orientada a conexión UDP**.
  * *No hay bloqueo*:
    * **Cola de mensajes**.
* **Traducción de datos**:
  * *Necesaria*:
    * **CORBA**.
