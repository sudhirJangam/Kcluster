from pymongo import MongoClient
from pymongo.operations import SearchIndexModel

# Connect to your Atlas deployment
mongodb_conn_string = "mongodb+srv://<UID>:<Pass>@mydb.sdiiymp.mongodb.net"

db_name = "complaints_db"
collection_name = "Complaints"
# Access your database and collection
client = MongoClient(mongodb_conn_string)
collection = client[db_name][collection_name]

# Create your index model, then create the search index
search_index_model = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "path": "embeddings",
                "numDimensions": 512,
                "similarity": "cosine"
            }
        ]
    },
    name="vector_index",
    type="vectorSearch",
)

#vcomp_index

result = collection.create_search_index(model=search_index_model)
print(result)