from entity.user import User

class LogoutController:

    def __init__(self):
        pass

    def logout(self, username:str) -> bool:
        return User.logout(username)
