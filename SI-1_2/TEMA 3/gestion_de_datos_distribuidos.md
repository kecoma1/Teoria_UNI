# Gestión de datos distribuidos

El concepto de "base de datos distribuida"/"base de datos como sistema distribuido" tiene varias acepciones:
* Un sistema cliente-servidor donde los datos se encuentran en un único o distintos servidores.
* Un sistema cliente-servidor o P2P donde los datos se encuentran en un sistema distribuido. Base de datos distribuida.

## Gestores de bases de datos
Sistema que se encarga de la organización, almacenamiento, gestión y recuperación (eficiente) de la información. En estos gestores se incluye:
* Un lenguaje para modelar la información de acuerdo a un determinado modelo (*__DDL__, Data Definition Language*).
* Estructuras de almacenamiento de la información optimizadas para trabajar con un **gran volumen de datos**.
* Un lenguaje para recuperar/manipular la información almacenada mediante busquedas dirigidas (*__DML__, Data Manipulation Language*).
* Los mecanismos adecuados que le permitan integrarse en un sistema de acceso con **control transaccional**.

En la actualidad, el modelo más habitual de gestores de bases de datos es el que sigue el **modelo relacional**, usando como lenguaje **SQL** (*Structured Query Language*). Hay que tener en cuenta que aunque hay una definicion ISO para SQL, cada SGBD tiene una versión con pequeñas diferencias.

Algunos ejemplos de gestores de bases de datos son: *IBM DB/2, Oracle, Sybase, Microsoft Access, Microsoft SQL Server, PostgreSQL, MySQL, MariaDB...*.

### Acceso de datos
En antaño, los datos se guardaban a través de un conjunto de ficheros. Los problemas con respecto a esta forma de guardar datos son los siguientes:
* **Volumetría**: Si se manejan muchos datos el fichero se hace enorme.
* **Redundancia** e **inconsistencia** en los datos.
* El acceso a los datos es **ineficiente** ya que existen varios formatos y la información puede estár duplicada en diferentes ficheros.
* Los datos **no están aislados** (esto significa que si la estructura de los datos varía hay que modificar los programas).
* Problemas de **integridad** ya que es difícil añadir nuevas restricciones o variar las que se establecieron inicialmente, y las restricciones tienen que ser reforzadas en cada programa y no por la base de datos.
* La **atomicidad** de las modificaciones es difícil de asegurar.
* Se debe permitir el **acceso simultáneo** para ganar velocidad de proceso, pero se a de asegurar que dos actualizaciones no son conflictivas.
* La **seguridad** es otro problema por que es difícil restringir parcialmente el acceso a datos.
  
## Bases de datos relacionales en entornos distribuidos

Una base de datos que se ajusta al modelo relacional puede representarse como un conjunto de tablas; a parte, los diagramas E-R (entidad-relación) pueden convertirse a tablas, este es el primer paso para obtener una base de datos relacional.

## Lenguajes de SQL

* **DDL**, lenguaje de definición de datos en el que se definen los *esquemas de relación*, *borrado de relaciones*, *creación de índices*, *modificación de esquemas de relación*, *Órdenes para la definición de vistas*, *Órdenes para especificar las restricciones de integridad que deben cumplir los datos almacenados en la base de datos*, *Órdenes para especificar derechos de acceso para las relaciones y vistas*... Se permite la creación y destrucción de tablas. En el DDL también se incluyen:
  * *Check*, restricción arbitraria.
  * *Not Null*, el atributo no acepta valores nulos.
  * *Unique*, el atributo no acepta valores repetidos.
  * *Primary key*, el atributo es clave primaria.
  * *Foreign key*, el atributo es clave extranjera.
* **DML**, lenguaje de manipulación de datos. Se incluye un lenguaje de consultas basado en álgebra relacional, se incluyen órdenes para insertar (*INSERT*), borrar (*DELETE/TRUCTATE*), modificar (*UPDATE*) y seleccionar (*SELECT*) (CRUD) tuplas en la base de datos.

### Agregaciones y agrupaciones
Las agregaciones más comunes son *SUM*, *AVG*, *MIN*, *MAX*, *COUNT*. Estos son operador que calculan un valor único a partir de una columna de valores. Las agregaciones se pueden aplicar mediante *filtros* o *agrupaciones*.

### Cruces de tablas (JOIN)
En un cruce se toman 2 o más relaciones y se obtiene otra relación, en principio con todos los atributos de las relaciones que se han cruzado.

**BUSCAR EN GOOGLE LOS DIFERENTES TIPOS DE JOIN**

### Combinación de relaciones (UNION, INTERSECT, EXCEPT)

Permite combinar 2 o más relaciones compatibles. Estos operadores por defecto eliminan las filas duplicadas, pero si se usa ALL estas no se eliminan.

### Subconsultas

Pueden aarecer subconsultas como parte de la condición descrita en la clausula WHERE, o en la clausula FROM sustituyendo una relación ya almacenada.

### Procesamiento de una consulta

1. Crear producto cartesiano descrito en FROM.
2. Aplicar las restricciones descritas en WHERE.
3. Si no hay GROUP BY, proyectar la relacion según select describe.
3.1 Agrupar las tuplas por valores tal y como especifica GROUP BY.
4. Aplicar HAVING.
5. Aplicar SELECT.

## Acceso a datos desde la aplicación

El **SQL interactivo** se define como el uso de SQL en el cliente del SGBD.

Las aplicaciones no acceden a datos almacenados en bases de datos relacionales a través de SQL interactivo si no a través de un *middleware*, el **driver de la base de datos**. Este driver es específico del SGBD y es un leguaje de alto nivel.

Existen varios **mecanismos de acceso de datos**:
* **SQL embebido** (inmerso/incrustado) en el código. Las sentencias SQL están incrustadas dentro del propio código mediante strings.
* **Sentencias preparadas**. Sentencia SQL precompilada que acepta parámetros, mejora el tiempo de respuesta y/o la seguridad, y es útil cuando una misma sentencia se utiliza varias veces.
* **DataSources lógicos**. Patrón de diseño que mejora la reusabilidad/mantenibilidad, y herramienta de acceso a datos que mejora los tiempos de acceso.

Estos mecanismos han *evolucionado*:
* Existe la **separación de responsabilidades** en el diseño. Esto mejora la legibilidad y la mantenibilidad del código. Se añaden frameworks y bibliotecas que permiten que las sentencias SQL no aparezcan inmersas en el código funcional.
* **ORM** *Object-Relational Mapping*. Es una abstracción del acceso a datos. Fue inicialmente parte del diseño de la aplicación, en la actualidad, en muchos casos se gestiona automáticamente. Son frameworks de persistencia que alamacenan y recuperan objetos de una base de datos relacional de forma transparente para el programador de la lógica de negocio. La capa de persistencia se invoca como a cualquier otro elemento de la lógica de negocio (el código SQL no existe).