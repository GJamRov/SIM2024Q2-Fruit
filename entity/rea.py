from entity.user import User

class REA(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)
