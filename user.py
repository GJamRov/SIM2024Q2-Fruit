# User Parent Class (user.py)

class User:

    def __init__(self, userID, username, password, email):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.logged_in = False

    def get_details(self):
        print(self.username, self.password)

    # User Story 1
    def login(self, entered_username, entered_password):
        """User Authentication"""
        if entered_username == self.username and entered_password == self.password:
            self.logged_in = True
            return True # Login Successful
        else:
            return False # Invalid Credentials
    
    # User Story 2
    def logout(self):
        """Logout the user"""
        self.logged_in = False
        return True # Logout successful
