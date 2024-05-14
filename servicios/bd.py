import pymongo

# Indicar IP y puerto
client = pymongo.MongoClient("localhost", 27017)

# También podemos indicar string de conexión
#client = pymongo.MongoClient("mongodb:localhost//localhost:27017")

# Accedemos a la BD
db = client["proyectoBDII"]

# Podemos acceder a las colecciones
examenes = db["examenes"]
categorias = db["categorias"]
indicaciones = db["indicaciones"]