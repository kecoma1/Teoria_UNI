# Transacciones

Es un concepto orientado a proveer tolerancia a fallos y permitir la concurrencia en sistemas distribuidos (en particular C/S).

_Una transacción es una colección de operaciones de lectura y escritura que están relacionados a nivel lógico._ Los requisitos son:
* Debe ocurrir en su totalidad o no ocurrir en absoluto (**Atomicidad**).
* Si la transacción se ejecuta, los efectos de las operaciones de escritura deben persistir; y si no se completa, la transacción no debe producir ningún efecto.
* Debe implementarse de forma que estos efectos se granticen _incluso si se produce un fallo del sistema_.

La concurrencia de transacciones genera fallos los cuales se pueden solucionar ejecutando las transacciones en "*serie*". En verdad, el objetivo es ejecutar las transacciones "de forma equivalente" a ejecutarlas en serie, pero no necesariamente en serie.

Decimos que una ejecución es correcta si **es en serie** o es **serializable** (que equivaldría a una ejecución en serie).

Se pueden obtener ejecuciones serializables a través de mecanismos de sincronización adecuados, como los **bloqueos (locks)**.