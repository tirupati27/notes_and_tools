from pymongo import MongoClient

uri = "mongodb://balaji274401:uIuX274401@ac-efsgriz-shard-00-00.ubtnqjz.mongodb.net:27017,ac-efsgriz-shard-00-01.ubtnqjz.mongodb.net:27017,ac-efsgriz-shard-00-02.ubtnqjz.mongodb.net:27017/?ssl=true&replicaSet=atlas-esbabp-shard-0&authSource=admin&retryWrites=true&w=majority&appName=web-cluster"


client = MongoClient(uri)
db = client["sample_mflix"]

# Test the connection
print(client.admin.command("ping"))
print(client.list_database_names())
print(db)
print(db.list_collection_names())



"""

{'ok': 1}

['sample_mflix', 'admin', 'local']

Database(MongoClient(host=['ac-efsgriz-shard-00-01.ubtnqjz.mongodb.net:27017', 'ac-efsgriz-shard-00-02.ubtnqjz.mongodb.net:27017', 'ac-efsgriz-shard-00-00.ubtnqjz.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, replicaset='atlas-esbabp-shard-0', authsource='admin', retrywrites=True, w='majority', appname='web-cluster', tls=True), 'sample_mflix')

['movies', 'comments', 'users', 'theaters', 'sessions', 'embedded_movies']

"""