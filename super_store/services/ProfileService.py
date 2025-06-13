from models.User import User
from enums.Role import Role

class ProfileService:
    def __init__(self):
        self.users = []
    
    def register(self,username,password,role:Role):
        for user in self.users:
            if user.username == username:
                print("user already exists")
                return None
        new_user = User(username,password,role)
        self.users += [new_user]
        print("user registered successfully")
        return new_user
    
    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.is_valid_password(password):
                print("login success")
                return user
        print("invalid credentials")
        return None
    
