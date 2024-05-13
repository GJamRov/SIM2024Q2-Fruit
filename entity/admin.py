# System Admin Class (admin.py)
# System Admins Class inherits from User Class
from entity.user import User

class SystemAdmin(User):
    
    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, 1, active)

    # Return all users to be displayed in users tab
    def view_all_user():
        SystemAdmin.connect_database("SampleDatabase")
        SystemAdmin.db.cursor.execute("SELECT * FROM User")
        users = SystemAdmin.db.cursor.fetchall()
        return users

    #3. Create user accounts
    def addUserAccount(self, newAccDetails)-> bool: 
        # Validate if the account already exists in the system
        if (SystemAdmin.db.search_one("User", f"username = '{newAccDetails[0]}'")):
            return False

        else: # Passes all checks
            # Create a new record and save it to database
            # f"NULL, '{username}', '{password}',  '{email}', {role}, {active}"
            details = f"NULL, '{newAccDetails[0]}', '{newAccDetails[1]}',  '{newAccDetails[2]}', {SystemAdmin.role_dict[newAccDetails[-1]]}, 1"
            SystemAdmin.db.insert_into_table("User", details)
            return True

    #4. View user accounts
    def view_account(self, entered_details="") -> list:
        if entered_details == "": # View all accounts
            search_result = SystemAdmin.db.view_table("User")
            return list(search_result)
        else:
            search_param =  f"username='{entered_details}'"
            search_result = SystemAdmin.db.search_one("User", search_param=search_param)
            return list(search_result)

    #5. Update user accounts
    def update_account(self, entered_details) -> bool:
        """Update User Account"""
        target_account = SystemAdmin.db.search_one("User", f"username = {entered_details[0]}")
        if target_account:
            update_details = ""
            # Update target_account with remaining information
            SystemAdmin.db.update_table("User", update_details, f"username = {entered_details[0]}")
            return True
        else:
            return False
        
    #6. Suspend user account
    def suspend_account(self, entered_username):
        """Suspend User Account in Database"""
        target_account = SystemAdmin.db.search_one("User", f"username = '{entered_username}'")
        if target_account:
            SystemAdmin.db.update_table("User", "active = 2", f"username = '{entered_username}'")
            return True
        else:
            return False