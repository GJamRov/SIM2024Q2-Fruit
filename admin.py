from user import User

class SystemAdmin(User):
    
    def __init__(self, userID, fname, lname):
        super().__init__(userID, fname, lname)

