import src.data.mongodb as mong
from src.models.user import User
from src.security.cripto_service import Security
db = mong.db

class User_services():
    
    def register_user(data=User(), password = None):
        dic = data.__dict__
        email = dic['_email'] 
        encoded_password = Security.start_encode(email, password)
        dic['password'] = encoded_password
        print(dic)
        db.users.insert(dic)

    def login_service(data):   
        user  = db.users.find_one({'_email': data['email']})
        decoded_password = Security.decode(user['_email'], user['password'])
        if decoded_password.decode() == data['password']:
            return user
        else: return 'wrong password'
        