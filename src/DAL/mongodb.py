from pymongo import MongoClient
client = MongoClient("mongodb+srv://carlos:root@cluster0.mm4nv.gcp.mongodb.net/api_python?retryWrites=true&w=majority")
db = client.cmstore  
    