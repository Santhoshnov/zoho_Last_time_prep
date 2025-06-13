class User:
    def __init__(self,username,password,role):
        self.username = username
        self.password = self.encrypt(password)
        self.role = role

    def encrypt(self,password):
        encrypted = ""
        for c in password:
            encrypted += chr((ord(c)+3) %256)
        return encrypted
    
    def is_valid_password(self,password_input):
        if self.encrypt(password_input) == self.password:
            return True