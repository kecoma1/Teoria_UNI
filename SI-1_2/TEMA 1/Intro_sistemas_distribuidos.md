# Sistemas distribuidos

### __Definición__
Podemos __definir__ un sistema distribuido como _una colección de elementos de computación autonomos que cooperan entre sí para resolver una tarea_.
Dentro de estos tenemos:
* **Sistema Centralizado**: Ordenador central y varios terminales que se conectan a este.
* **Sistema Distribuido**: Como se ha mencionado antes, elementos independientes no necesariamente homogéneos interconectados por una red de cualquier tipo. Dan la apariencia de un sistema único.

Este esquema permite la distribución inherente de aplicaciones, compartir recursos, acceso a recursos remotos y la relación rendimiento-coste mejora ya que varios nodos siempre van a ser mejor que uno.

### __Desventajas__
Los sistemas distribuidos tienen __desventajas__ como:
* *Un aumento de complejidad*.
* *Las comunicaciones causan errores*.
* *Difícil garantizar la seguridad*.
* *Difícil garantizar la confidencialidad*.

### __Transparencia__

Los sistemas distribuidos __deben__ ser transparentes para así dar apariencia de un sistema único y coherente a sus usuarios. Para esto es necesario que:
* El *acceso* para el usuario sea el mismo (o parecido) al que tendría localmente.
* La *localización* no sea importante.
* La *replicación* sea posible, un sistema debe poder replicarse en cualquier otro lugar.
* Sea *concurrente* permitiendo a varios usuarios acceder.
* Pueda *ocultar (o intentarlo)* fallos.
* Sea *escalable*.

### __¿Como se coordinan los SD (Sistemas Distribuidos)?__
### Software
Se pueden coordinar _temporalmente_ (funcionan al mismo tiempo) y _referencialmente_ (en el mismo espacio). Si ambas partes se cumplen decimos que el acoplamiento es __directo__.
Pero puede ocurrir que tengamos _desacoplamiento referencial_, donde los nodos no se conocen (no saben la dirección de los otros), o podemos también tener _desacoplamiento temporal_ donde los nodos no están activos al mismo tiempo.
### Hardware
Pueden estar _fuertemente acoplados_ donde se comparte la memoria, buses... o pueden estar _débilmente acoplados_ donde los procesadores son autónomos y están interconectados por sistemas de comunicaciones.

### __Principales modelos__
__Cliente-Servidor__: Es un sistema asimétrico (1 servidor grande, clientes pequeños), los clientes solicitan servicios y los servidores los ejecutan devolviendo resultados.

__Igual a igual (P2P)__: El sistema es simétrico (todos los nodos hacen de servidor y de cliente), todos los procesos desempeñan tareas semejantes e interactuan para realizar una actividad distribuida.

# Arquitectura de los sistemas distribuidos
## Arquitectura software
La arquitectura software de un SI define el sistema en términos de __componentes__ e __interacciones__ entre ellos. Los componentes pueden ser el _cliente_, el _servidor_, la _base de datos_... Las interacciones se identifican por la _ubicación_ de cada componente y la _distribuición_ de los datos. Las interacciones pueden ser _llamadas a procedimientos_, _mensajes_, _compartición de variables_, _protocolos cliente/servidor_, _protocolos de acceso a la BB.DD._...

La arquitectura software de un SI puede ser abstracta, lo que permite que se pueda reutilizar en otro sistema.

Dependiendo de la aplicación la arquitectura SW que se considera es una u otra:
* **P2P**
* **Cliente-Servidor**

El objetivo de diseño de los SD es:
* Compartir y optimizar el uso de recursos.
* Transparencia.
* Sistema abierto.
* Escalabilidad.

Hay que tener en cuenta que:
* Las comunicaciones __NO__ son confiables.
* Las comunicaciones __NO__ son seguras.
* __EXISTEN__ restricciones en el ancho de banda.
* La red __NO__ es homogénea.
* La infraestructura/topología __SÍ__ cambia.
* La latencia __NO__ es despreciable.
* El coste añadido por la capa de transporte __NO__ es despreciable.
* El coste económico de una infraestructura distribuida es siempre __MAYOR__.
* __NO__ hay un único administrador.

En los modelos arquitectónicos tenemos los conceptos de:
* **Capa**: Se refiere al Software.
* **Nivel**: Se refiere al Hardware.

Las arquitecturas tradicionales de 3 capas tienen:
* Una **capa de interfaz de usuario**.
* Una **Capa de procesamiento**.
* Una **Capa de datos**.

Las arquitecturas también se pueden dividir en niveles (hay que tener en cuenta que este esquema no siempre es exactamente así):
* **1 nivel**: Todo el procesamiento y la gestión de los datos se hace en un único terminal (peluquería).
* **2 niveles**: Tenemos los clientes y luego un servidor/base de datos.
* **3 niveles**: Tenemos los clientes, luego servidores que almacenan la lógica de negocio y por último una base datos.

## Arquitecturas orientadas a objetos y servicios
En la __Arquitectura Orientada a Objetos__ el sistema está compuesto de objetos que se conectan mediante llamadas a procedimientos. Cada objeto puede estar una máquina diferente, y los objetos encapsulán datos y ofrecen métodos para manipularlos sin revelar la implementación interna.

La __Arquitectura Orientada a Servicios__ (__SOA__, siglas del inglés _Service Oriented Architecture_) es un estilo de arquitectura de TI que se apoya en la orientación a servicios. La orientación a servicios es una forma de pensar en servicios, su construcción y sus resultados. Un servicio es una representación lógica de una actividad de negocio que tiene un resultado de negocio específico (ejemplo: comprobar el crédito de un cliente, obtener datos de clima, consolidar reportes de perforación).

El estilo de arquitectura SOA se caracteriza por:
* Estar basado en el diseño de servicios que reflejan las actividades del negocio en el mundo real, estas actividades forman parte de los procesos de negocio de la compañía.
* Representar los servicios utilizando descripciones de negocio para asignarles un contexto de negocio.
* Tener requerimientos de infraestructura específicos y únicos para este tipo de arquitectura, en general se recomienda el uso de estándares abiertos para la interoperabilidad y transparencia en la ubicación de servicios.
* Estar implementada de acuerdo con las condiciones específicas de la arquitectura de TI en cada compañía.
* Requerir un gobierno fuerte sobre las representación e implementación de servicios.
* Requerir un conjunto de pruebas que determinen que es un buen servicio.

## Arquitectura Orientada a Recursos
Esta arquitectura surge para facilitar la integración de servicios en arquitecturas SOA. El sistema distribuido se ve como una colección de recursos, gestionados individualmente por componentes. Los recursos pueden ser añadidos, eliminados, obtenidos y modificados remota y dinámicamente por las aplicaciones. Se utiliza ampliamente en las arquitecturas __RESTful__.

## Arquitecturas Basadas en Eventos.
Campanita youtube, publicaciones, suscripciones...

Separan el procesamiento y la coordinación. Los procesos operan de manera autónoma debido al:
* **Desacoplamiento temporal**: Los sistemas son asíncronos ya que la respuesta puede darse en un espacio de tiempo variable después de la llamada.
* **Desacoplamiento referencial**: No es necesario conocer de antemano la referencia.
  
# Componentes Software de un Sistema Distribuido
Se suelen considerar 3 módulos principales:
* **El cliente**. Es aquel __proceso__ que solicita y consume servicios. Hay que tener en cuenta que un servidor también puede ser cliente de otro servidor. La funcionalidad del proceso cliente marca la operativa de la aplicación. 
* **Middleware**. Enlace entre cliente y servidor o entre servidores. Se considera el "sistema operativo" de los sistemas distribuidos. Se ejecuta sobre el sistema operativo local tanto en el servidor como en el cliente. No depende del hardware ni del sistema operativo subyacente. La interfaz suele ser Cliente/Servidor o Servidor/Servidor.
* **Servidor**. Todo aquel proceso que proporciona servicios.
  
Los middlewares suelen tener 3 capas:
* Protocolo especifico de servicio (ODBC, Correo, HTTP...).
* Network Operating System, NOS (Directorio, seguridad, tiempo, API directa...).
* Transporte (TCP/IP, IPX/SPX...)