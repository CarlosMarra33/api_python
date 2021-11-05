from flask import request
from bson.json_util import dumps
from src.server.instance import server
from src.models.product import Product
from src.data.product_services import Products_services as mongo

app = server.app


class Product_Controller:
    @app.route("/")
    def initialize():
        return "olá mundo"

    @app.route("/produto/buscar/nome", methods=["GET"])
    def teste():
        body = request.get_json()
        print(body)

        return dumps(mongo.find_product(body))

    @app.route("/produto/buscar", methods=["GET"])
    def find_all_products():
        return dumps(mongo.find_all_products())

    @app.route("/produto/criar", methods=["POST"])
    def teste_post():
        body = request.get_json()
        try:
            if mongo.find_product({"name": body["name"]}) != None:
                product = Product(
                    body["name"],
                    body["description"],
                    body["price"],
                    body["qtd"],
                    body["category"],
                    body["img"],
                )
                response_mongo = mongo.add_products(product)
        except print(0):
            pass
