from entity.user import User

class LoginController:

    def __init__(self):
        pass

    def validateLogin(self, username:str, password:str) -> int:
        return User.login(username, password)
    