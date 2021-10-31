from flask import request
from bson.json_util import dumps
from src.server.instance import server
from src.models.product import Product
from src.DAL.mongodb import Mongo as mongo
app = server.app


class Produto():
    @app.route('/')
    def initialize():
        return "olá mundo"

    @app.route('/produto/buscar/nome', methods=['GET'])
    def teste():
        body = request.get_json()
        print(body)
        
        return dumps(mongo.find_products(body))

    @app.route('/produto/buscar', methods=['GET'])
    def find_all_products():
        return dumps(mongo.find_all_products())

    @app.route('/produto/criar', methods=['POST'])
    def teste_post():
        body = request.get_json()
        product = Product(name=body['name'], description=body['description'], price=body['price'],
        qtd=body['qtd'], category=body['category'], img=body['img'])
        response_mongo = mongo.add_products(product)
        if response_mongo == 200:
            return "adcionado"  
        else:
            return "já exite esse produto"
    

    


