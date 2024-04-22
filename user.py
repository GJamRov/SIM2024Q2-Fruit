# User Parent Class

class User:

    def __init__(self, userID, username, password, role, email):
        self.userID = userID
        self.username = username
        self.password = password
        self.role = role
        self.email = email
        self.logged_in = False

    #TODO: User Story 1
    def login(self, username, password, database):
        #  User Authentication
        return True
    
    #TODO: User Story 2
    def logout(self):
        """Logout the user"""
        self.logged_in = False