# System Admin Class (admin.py)
# System Admins Class inherits from User Class
from entity.user import User

class SystemAdmin(User):
    
    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)

    #TODO: 3. Create user accounts
    def create_account(self, userAcc, db):
        if userAcc.username in self.username:
            return False 
        elif userAcc.password != userAcc.confirm_password:
            return False 
        else:
            self.username = userAcc.username
            self.password = userAcc.password
            self.email = userAcc.email
            return True #Account created

    #TODO: 4. View user accounts
    def view_account(self, entered_username, db) -> list:
        if entered_username == self.username:
            return [self.userID, self.username, self.email]
        else:
            return []

    #TODO: 5. Update user accounts
    def update_account(self, db):
        pass
        

    #TODO: 6. Suspend user account
    def suspend_account(self, entered_username, db):
        # Suspend user in database (add is_active column to table)
        # cursor = db_connection.cursor()
        # query = "UPDATE sample_db SET is_active = FALSE WHERE username = %s"
        # cursor.execute(query, (entered_username,))
        # db_connection.commit()
        # Check if the update affected any rows
        #if cursor.rowcount > 0:
        #    return True  # Suspend successful
        #else:
        #    return False  # User not found or already suspended
        pass

    #TODO: 8. Create user profiles
    def create_profile(self, db_connection):
        pass

    #TODO: 9. View user profiles
    def view_profile(self, db_connection):
        pass

    #TODO: 11. Suspend user profile
    def suspend_profile(self, db_connection):
        pass

    #TODO: 12. Search user profile
    def search_profile(self, db_connection):
        pass
