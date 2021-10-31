from src.models.product import Product
import src.DAL.mongodb as mong
db = mong.db
class Products_services():
    
    def add_products(data=Product()):
        db.products.insert(data.__dict__)
        
    def find_product(data):
        return db.products.find_one(data)

    def find_all_products():
        return db.products.find()