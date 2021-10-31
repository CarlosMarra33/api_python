from pymongo import MongoClient

import json
from src.models.product import Product
client = MongoClient("mongodb+srv://carlos:root@cluster0.mm4nv.gcp.mongodb.net/api_python?retryWrites=true&w=majority")
db = client.cmstore
class Mongo():


    def add_products(data):
        collection = db.products.count(data.__dict__)
        if collection == 0:
            db.products.insert(data.__dict__)
            return 200
        else:
            pass
    
    def find_products(data):
        return db.products.find_one(data)

    def find_all_products():
        return db.products.find()
    