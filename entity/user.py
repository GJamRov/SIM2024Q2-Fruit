# User Parent Class (user.py)
import database

class User:

    def __init__(self, userID, username, password, email, role, active, logged_in):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.active = active
        self.logged_in = 0

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
    def login(entered_username, entered_password):
        """User Authentication"""
        db =  database.Database("SampleDatabase")
        db.cursor.execute("SELECT * FROM User WHERE username = ?", (entered_username,))
        user_data = db.cursor.fetchone()

        if user_data:
            self = User(*user_data)
            if entered_username == self.username and entered_password == self.password:
                db.cursor.execute("UPDATE User SET logged_in = 1 WHERE username = ?", (entered_username,))
                db.connection.commit()
                db.cursor.close()
                return self.role # Login Successful
            else:
                return 0 # Invalid Credentials
    
    # User Story 2
    def logout(username):
        """Logout the user"""
        db =  database.Database("SampleDatabase")
        db.cursor.execute("SELECT * FROM User WHERE username = ?", (username,))
        user_data = db.cursor.fetchone()

        if user_data:
            self = User(*user_data)
            if username == self.username:
                db.cursor.execute("UPDATE User SET logged_in = 0 WHERE username = ?", (username,))
                db.connection.commit()
                db.cursor.close()
        return True # Logout successful
