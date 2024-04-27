from entity.user import User

class Seller(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)
