# Diagrama peliculas

![diagrama-peliculas](Ej1_diagrama.drawio.png)

# Diagrama banco

![diagrama-banco](Ej2_diagrama.drawio.png)

### Ejercicio 1

> a) *Crea la BD en PostgreSQL a partir del script proporcionado.*

Instrucctiones en la carpeta SI-1_2/BD

> b) *¿Qué relaciones se establecen entre cada entidad (cardinalidad)?*

Tenemos una cardinalidad 1-N, **cada actor aparece en N películas**.

#### Base de datos banco
Tenemos la relación cliente_cuenta donde **por cada cliente tenemos N cuentas**. 

Tenemos también la relación cliente_prestamo donde **por cada cliente tenemos N prestamos**.

> c) *¿Por qué la tabla REPARTO tiene una clave primaria compuesta por ACTOR_ID y PELICULA_ID?*

No se puede usar una de las 2 foreign-keys como clave primaria ya que **se repetetiría** dentro de la propia relación. En cambio si usamos ambas claves no encontramos repeticiones y podemos hacer única la relación entre una película y un actor.

> d) *¿Por qué el orden de creación de las tablas debe ser: ACTOR o PELICULA, y luego
REPARTO?* 

Porque al crear la tabla reparto referenciamos las claves primarias de ACTOR y PELICULA, y no tendría sentido referenciar algo inexistente.

> e) *¿Por qué el orden de borrado de las tablas debe ser: REPARTO, y luego ACTOR o
PELICULA?*

Porque si tratamos de borrar ACTOR o PELICULA antes que REPARTO, al no permitir a las foreign keys de ACTOR y PELICULA en la tabla REPARTO sean NULL, estaríamos borrando algo referenciado desde otra tabla y esto provocaría un error ya que el la clave no puede ser NULL.

### Ejercicio 2

