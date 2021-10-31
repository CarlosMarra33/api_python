import src.DAL.mongodb as mong
from src.models.user import User
db = mong.db
class User_services():
    def register_user(data=User()):
        db.users.insert(data.__dict__)

    def get_user_by_email(email):   
        return db.users.find_one(email)

