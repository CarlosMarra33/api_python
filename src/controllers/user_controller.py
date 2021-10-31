from flask import request
from bson.json_util import dumps
from src.server.instance import server
from src.models.user import User
from src.models.endereco import Endereco
from src.DAL.user_services import User_services as mongo
app = server.app

class User_controller():
    
    @app.route('/user/register', methods=['POST'])
    def register():
        body = request.get_json()
        try:
            if mongo.get_user_by_email({'email': body['email']} != None):
                user = User(body['name'], body['email'], body['cpf'],
                body['cep'], body['password'])
                user.add_endereco(Endereco(body['street'], body['number'],
                body['complement']))
                mongo.register_user(user)
        except print(0):
            pass

    @app.route('/user/login', methods=['POST'])
    def login():
        body = request.get_json()
        # ! body para login tem que ser email e password
        try:
            mongo.get_user_by_email(body)
        except print(0):
            pass   