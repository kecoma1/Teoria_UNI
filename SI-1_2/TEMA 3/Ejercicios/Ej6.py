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