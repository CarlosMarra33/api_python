from flask import request
from bson.json_util import dumps
from src.server.instance import server
from src.models.user import User
from src.models.endereco import Endereco
from src.data.user_services import User_services as mongo
app = server.app

class User_controller():
    
    @app.route('/user/register', methods=['POST'])
    def register():
        body = request.get_json()
        print(body)
        try:
            if mongo.check_user({'email': body['email']} == 0):
                user = User(body['name'], body['email'], body['cpf'],
                body['cep'])
                mongo.register_user(user, body['password'])
            else:
                return 'email já existe'
        except print(0):
            pass
        return 'user registrado'

    @app.route('/user/login', methods=['POST'])
    def login():
        body = request.get_json()
        # ! body para login tem que ser email e password
        try:
            user= mongo.login_service(body)
            return user
        except print(0):
            pass   
        return 'login'

    @app.route('/user/profile', methods = ['GET'])
    def user_profile():
        body = request.get_json()
        
        return mongo.get_user(body['_email'])
    
    @app.route('/user/prifle/edit', methods = ['PUT'])
    def edit_user_profile():
        body = request.get_json()
        try:
            return mongo.edit_user_profile(body)    
        except Exception as e:
            return '500'
        
        


        
        