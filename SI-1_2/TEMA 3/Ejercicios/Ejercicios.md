# Diagrama peliculas

![diagrama-peliculas](Ej1_diagrama.drawio.png)

# Diagrama banco

![diagrama-banco](Ej2_diagrama.drawio.png)
***En prestamo -> saldo, no es eso, es prestamo -> cantidad***

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

> d) *¿Por qué el orden de creación de las tablas debe ser: ACTOR o PELICULA, y luego REPARTO?* 

Porque al crear la tabla reparto referenciamos las claves primarias de ACTOR y PELICULA, y no tendría sentido referenciar algo inexistente.

> e) *¿Por qué el orden de borrado de las tablas debe ser: REPARTO, y luego ACTOR o PELICULA?*

Porque si tratamos de borrar ACTOR o PELICULA antes que REPARTO, al no permitir a las foreign keys de ACTOR y PELICULA en la tabla REPARTO sean NULL, estaríamos borrando algo referenciado desde otra tabla y esto provocaría un error ya que el la clave no puede ser NULL.

### Ejercicio 2

a) *Crea una consulta que muestre los nombres de los clientes que tienen un préstamo en la sucursal Perryridge, pero que no tengan una cuenta en dicha sucursal.*

```sql
-- Prestamos cliente
select cl.id, cl.nombre_cliente, pr.numero_prestamo, pr.nombre_sucursal 
from cliente as cl, cliente_prestamo as cl_pr, prestamo as pr
where cl.id = cl_pr.id_cliente AND pr.numero_prestamo = cl_pr.numero_prestamo

-- Cuentas cliente
select cl.id, cl.nombre_cliente, cu.numero_cuenta, cu.nombre_sucursal 
from cliente as cl, cliente_cuenta as cl_cu, cuenta as cu
where cl.id = cl_cu.id_cliente AND cu.numero_cuenta = cl_cu.numero_cuenta

-- Juntamos todo
select t1.t1_nombre_cliente
from 
	(select cl.id as t1_id_cliente, cl.nombre_cliente as t1_nombre_cliente, pr.numero_prestamo, pr.nombre_sucursal as t1_nombre_sucursal
	from cliente as cl, cliente_prestamo as cl_pr, prestamo as pr
	where cl.id = cl_pr.id_cliente AND pr.numero_prestamo = cl_pr.numero_prestamo) as t1,
	(select cl.id as t2_id_cliente, cl.nombre_cliente, cu.numero_cuenta, cu.nombre_sucursal as t2_nombre_sucursal
	from cliente as cl, cliente_cuenta as cl_cu, cuenta as cu
	where cl.id = cl_cu.id_cliente AND cu.numero_cuenta = cl_cu.numero_cuenta) as t2
where t1.t1_id_cliente = t2.t2_id_cliente AND t1.t1_nombre_sucursal = 'Perryridge' AND NOT t2.t2_nombre_sucursal = 'Perryidge';
```

b) *Crea una consulta que muestre, en franjas de 1000 en 1000, el número de prestamos cuyo monto (cantidad) esté en cada una de las franjas.*

```sql
-- Valor prestamo
select cantidad, count(cantidad)
from prestamo
group by cantidad
```
Ni idea, habría que agrupar de alguna forma.

c) *Crea un procedimiento almacenado, llamado busqueda, que dado el nombre de una ciudad muestre los clientes que tienen cuenta en alguna sucursal de dicha ciudad, pero que vivan (los clientes) en otra ciudad distinta.*

```sql
-- Procedimiento almacenado
CREATE OR REPLACE FUNCTION busqueda(ciudad VARCHAR)
RETURNS TABLE (
		nombre_cliente VARCHAR
	) AS $$
BEGIN
	RETURN QUERY select cl.nombre_cliente
	from cliente as cl, cliente_cuenta as cl_cu, cuenta as cu, sucursal as s
	where s.ciudad_sucursal = ciudad and NOT cl.ciudad_cliente = ciudad and cu.nombre_sucursal = s.nombre_sucursal
	and cl.id = cl_cu.id_cliente and cl_cu.numero_cuenta = cu.numero_cuenta;
END;
$$ LANGUAGE plpgsql;

-- Probamos el procedimiento
select * from busqueda('Brooklyn')
```

### Ejercicio 6

```py
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db"]
universidades = db["universidades"]

uam = {
		"nombre": "Universidad autonoma de madrid",
		"direccion-postal": 15123,
		"fecha-apertura": 1999, # Ni idea
		"alumnos": 30000, # Ni idea
		"telefono": 12345678,
		"email": "uam@uam.es",
		"web": "www.uam.es",
		"facultades": [
			{"nombre": "Ciencias"},
			{"nombre": "Biologia"},
			{"nombre": "Derecho"},
			{"nombre": "Economicas"},
			{"nombre": "Politécnica"}
		]
	  }

ucm = {
		"nombre": "Universidad complutense de madrid",
		"direccion-postal": 11111,
		"fecha-apertura": 1998, # Ni idea
		"alumnos": 20000, # Ni idea
		"telefono": 12343678,
		"email": "ucm@ucm.es",
		"web": "www.ucm.es",
		"facultades": [
			{"nombre": "Ciencias"},
			{"nombre": "Biologia"},
			{"nombre": "Derecho"},
			{"nombre": "Economicas"},
			{"nombre": "Politécnica"}
		]
	  }

uc3m = {
		"nombre": "Universidad Carlos 3º de madrid",
		"direccion-postal": 11211,
		"fecha-apertura": 1993, # Ni idea
		"alumnos": 25000, # Ni idea
		"telefono": 11343678,
		"email": "uc3m@uc3m.es",
		"web": "www.uc3m.es",
		"facultades": [
			{"nombre": "Ciencias"},
			{"nombre": "Biologia"},
			{"nombre": "Economicas"},
			{"nombre": "Politécnica"}
		]
	  }

# Borramos un único documento en una llamada
universidades.delete_one({"nombre": "Universidad autonoma de madrid"})
universidades.delete_one({"nombre": "Universidad complutense de madrid"})
universidades.delete_one({"nombre": "Universidad Carlos 3º de madrid"})

# Borramos todos los documentos
# universidades.delete_many(
# 	{"nombre": [
# 		"Universidad autonoma de madrid", 
# 		"Universidad complutense de madrid", 
# 		"Universidad Carlos 3º de madrid"
# 		]
# 	},
# )

# Insertamos las universidades en una única llamada
universidades.insert_many([uam, ucm, uc3m])

# Insertarlas de una en una
# universidades.insert_one(uam)
# universidades.insert_one(ucm)
# universidades.insert_one(uc3m)

# Query 1: Todas las facultades de la UAM
result = universidades.find({"nombre": "Universidad autonoma de madrid"}, {"facultades": 1})
print("[QUERY 1]: ")
for res in result:
	print(res)
print("\n")

# Query 2: Total estudiantes de cada universidad
result = universidades.find({}, {"nombre": 1, "alumnos": 1})
print("[QUERY 2]: ")
for res in result:
	print(res)
print("\n")

# Query 3: Universidades con facultad de derecho
result = universidades.find({"facultades": { "$in" : [{"nombre": "Derecho"}]}}, 
							{"nombre": 1})
print("[QUERY 3]: ")
for res in result:
	print(res)
```