from json import dumps
import src.data.mongodb as mong
from src.models.user import User
from src.security.cripto_service import Security

db = mong.db


class User_services:
    def register_user(data=User(), password=None):
        dic = data.__dict__
        email = dic["_email"]
        encoded_password = Security.start_encode(email, password)
        dic["password"] = encoded_password
        print(dic)
        db.users.insert(dic)

    def login_service(data):
        result = db.users.find_one({"_email": data["email"]})
        decoded_password = Security.decode(
            result["_email"], result["password"]
        )
        if decoded_password.decode() == data["password"]:
            user = User(
                result["_name"],
                result["_email"],
                result["_cpf"],
                result["_cep"],
                result["_endereco"],
            )
            return dumps(user)
        else:
            return 500

    def get_user(data):
        return db.users.find_one({"_email": data})

    def edit_user_profile(data):
        query = {"_email": data["email"]}
        updated_user = {"$set": data}
        db.users.update_one(query, updated_user)
        return "200"
