# Sistemas distribuidos

### __Definición__
Podemos __definir__ un sistema distribuido como _una colección de elementos de computación autonomos que cooperan entre sí para resolver una tarea_.
Dentro de estos tenemos:
* **Sistema Centralizado**: Ordenador central y varios terminales que se conectan a este.
* **Sistema Distribuido**: Como se ha mencionado antes, elementos independientes no necesariamente homogéneos interconectados por una red de cualquier tipo. Dan la apariencia de un sistema único.

Este esquema permite la distribución inherente de aplicaciones, compartir recursos, acceso a recursos remotos y la relación rendimiento coste mejora ya que varios nodos siempre van a ser mejor que uno.

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


  