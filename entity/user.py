# User Parent Class (user.py)
import database

class User:

    # Static Variable
    db =  database.Database("SampleDatabase")
    role_dict = {
                "System Admin":1,
                "REA":2,
                "Buyer":3,
                "Seller":4
                }

    def __init__(self, userID, username, password, email, role, active):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.active = active

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
    
    ## Setter methods
    def set_username(self, new_username):
        self.username = new_username
    
    def set_password(self, new_password):
        self.password = new_password
    
    def set_email(self, new_email):
        self.email = new_email
    
    def set_status(self, new_status):
        self.active = new_status

    ## Static Methods
    # User Story 1
    def login(entered_username, entered_password) -> int:
        """Authenticates user to log them in"""
        user_data = User.db.search_one("User", f"username = '{entered_username}'")

        if user_data:
            self = User(*user_data)
            if entered_username == self.username and entered_password == self.password and self.active == 1:
                return self.role # Login Successful (Valid credentials and active account)
            elif entered_username == self.username and entered_password == self.password and self.active == 2:
                return 5 # Valid credentials but suspended account
            elif entered_username != self.username or entered_password != self.password:
                return 6 # Invalid credentials
