> Para crear una base de datos:
```
createdb -U alumnodb <nombre base de datos>
```

> Para ejecutar un script:
```
cat miscript.sql | psql -U alumnodb <nombre base de datos>
```


### Si no tienes instalado postgres haz esto:

```
sudo apt-get update
sudo apt-get install postgresql
sudo gedit /etc/postgresql/12/main/pg_hba.conf
```

> Añadir estas líneas al archivo
```
local all alumnodb md5
host all alumnodb 127.0.0.1/32 md5
```
> Guardar

```
sudo gedit /etc/postgresql/12/main/postgresql.conf
```
> Haz ctrl+f busca esas variables y descomentalas y dalas esos valores

```
autovacuum_vacuum_threshold = 5000000
autovacuum_analyze_threshold= 5000000
```
```
sudo systemctl restart postgresql
sudo su - postgres
```
> Dentro de la terminal de postgres
```
createuser -s alumnodb
psql
\password alumnodb
```
ctrl+d para salir

### Ya está

