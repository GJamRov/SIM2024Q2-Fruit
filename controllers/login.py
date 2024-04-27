from entity.user import User

class LoginController:

    def __init__(self, user_db):
        self.user_db = user_db

    def validateLogin(self, username:str, password:str) -> bool:
        user = self.search_user(username)
        if user:
            return user.login()
        else:
            return False

    def search_user(self, username:str):
        for  u in self.user_db:
            if u.getUsername() == username:
                return u
        return None