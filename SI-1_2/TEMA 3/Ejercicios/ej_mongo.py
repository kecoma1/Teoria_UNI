import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["db"]
personas = db["personas"]

personas.delete_one({"nombre": "Andrea"})
personas.delete_one({"nombre": "Jose"})
personas.delete_one({"nombre": "Maria"})
personas.delete_one({"nombre": "Luis"})

personas.insert_many([
	{
		"nombre": "Andrea",
		"apellidos": "Martinez Santos",
		"edad": 30,
		"casado": True,
		"aficiones": [
			{"nombre": "Alpinismo", "coste": 300},
			{"nombre": "Ajedrez", "coste": 60}
		],
	},
	{
		"nombre": "Jose",
		"apellidos": "Santos Perez",
		"edad": 26,
		"casado": True,
		"aficiones": [
			{"nombre": "Judo", "coste": 300},
			{"nombre": "Boxeo", "coste": 200}
		],
	},
	{
		"nombre": "Maria",
		"apellidos": "Martin Gutierrez",
		"edad": 27,
		"casado": False,
		"aficiones": [
			{"nombre": "Boxeo", "coste": 100},
			{"nombre": "Ajedrez", "coste": 50},
			{"nombre": "Yoga", "coste": 30}
		],
	},
	{
		"nombre": "Luis",
		"apellidos": "Garcia Marcos",
		"edad": 24,
		"casado": False,
		"aficiones": [
			{"nombre": "Paracaidismo", "coste": 400},
			{"nombre": "Esgrima", "coste": 200},
			{"nombre": "Boxeo", "coste": 500}
		],
	},
])

print("[QUERY 1]: Nombre personas y el coste total de sus aficiones pero solo de aquellas personas que se gastan menos de 400 en total")

res = personas.aggregate([
	{
		"$project": { 
			"_id": 0,
			"nombre": 1,
			"Coste Total Aficiones": {"$sum": "$aficiones.coste"}
		}
	},
	{
		"$match": {
			"Coste Total Aficiones": {"$lt": 400}
		}
	}
])

for r in res:
	print(r)

print("\n[QUERY 2]: Nombre y apellidos que no tengan alpinismo ni paracaidismo y estén solteras")

res = personas.find({
	"$nor": [
		{"aficiones.nombre": "Paracaidismo"},
		{"aficiones.nombre": "Alpinismo"}
	],
	"casado": False
}, {"_id": 0, "nombre": 1, "apellidos": 1})

for r in res:
	print(r)

print("\n[QUERY 3]: Aficion mas barata de cada persona y el nombre de la persona")

res = personas.aggregate(
	[
		{
			"$project": {
				"_id": 0,
				"nombre": 1,
				"Coste aficion mas barata": {
					"$min": "$aficiones.coste"
				}
			}
		},
	]
) 

for r in res:
	print(r)