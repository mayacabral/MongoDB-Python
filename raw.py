from pymongo import MongoClient

connection_String = "mongodb://mayaragcabral:1234@ac-uviifkt-shard-00-01.qpwswdk.mongodb.net:27017,ac-uviifkt-shard-00-02.qpwswdk.mongodb.net:27017,ac-uviifkt-shard-00-00.qpwswdk.mongodb.net:27017/admin?ssl=true&retryWrites=true&loadBalanced=false&replicaSet=atlas-5o4v36-shard-0&readPreference=primary&connectTimeoutMS=10000&w=majority&authSource=admin&authMechanism=SCRAM-SHA-1"
client = MongoClient(connection_String)
db_connection = client['atlas']


collection = db_connection.get_collection("admin")

#print(collection)

search_filter = { "nome" : "Mayara"}

response = collection.find(search_filter)
print(response)

for registry in response: print(registry)

collection.insert_one({
    "Estou":"inserindo",
    "numeros": [123,456,789]
})