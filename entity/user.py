# User Parent Class (user.py)

class User:

    def __init__(self, userID, username, password, email, active):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.active = active
        self.logged_in = False

    ## Getter & Setter
    def get_id(self):
        return self.userID
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_email(self):
        return self.email
    
    def get_status(self):
        return self.active
    
    def get_login_status(self):
        return self.logged_in
    
    ## Setter methods
    def set_username(self, new_username):
        self.username = new_username
    
    def set_password(self, new_password):
        self.password = new_password
    
    def set_email(self, new_email):
        self.email = new_email
    
    def set_status(self, new_status):
        self.active = new_status
    
    def set_login_status(self, new_login_status):
        self.logged_in = new_login_status

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
