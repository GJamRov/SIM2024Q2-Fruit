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
    def addUserAccount(newAccDetails)-> bool: 
        SystemAdmin.connect_database("SampleDatabase")
        # Validate if the account already exists in the system
        if (SystemAdmin.db.search_one("User", f"username = '{newAccDetails[0]}'")):
            return False

        else: # Passes all checks
            # Create a new record and save it to database
            # f"NULL, '{username}', '{password}',  '{email}', {role}, {active}"
            details = f"NULL, '{newAccDetails[0]}', '{newAccDetails[1]}',  '{newAccDetails[2]}', {newAccDetails[3]}, 1"
            SystemAdmin.db.insert_into_table("User", details)
            return True

    #4. View user accounts
    def view_account(account=""):
        if account == "": # View all accounts
            search_result = SystemAdmin.db.view_table("User")
            return search_result
        else:
            search_param =  f"username='{account}'"
            search_result = SystemAdmin.db.search_one("User", search_param=search_param)
            return search_result

    #5. Update user accounts
    def update_account(entered_details) -> bool:
        """Update User Account"""
        SystemAdmin.connect_database("SampleDatabase")
        account_data = SystemAdmin.db.search_one("User", f"username = '{entered_details[0]}'")
        if account_data:
            update_details = f"username = '{entered_details[1]}', password = '{entered_details[2]}', email = '{entered_details[3]}', role = {entered_details[4]}"
            # Update target_account with remaining information
            SystemAdmin.db.update_table("User", update_details, f"username = '{entered_details[0]}'")
            return True
        else:
            return False
        
    #6. Suspend user account
    def suspend_account(entered_username):
        """Suspend User Account in Database"""
        SystemAdmin.connect_database("SampleDatabase")
        target_account = SystemAdmin.db.search_one("User", f"username = '{entered_username}'")
        if target_account:
            SystemAdmin.db.update_table("User", "active = 2", f"username = '{entered_username}'")
            return True
        else:
            return False
        
    #13. Reactivate user account
    def reactivate_account(entered_username):
        """Reactivate User Account in Database"""
        SystemAdmin.connect_database("SampleDatabase")
        target_account = SystemAdmin.db.search_one("User", f"username = '{entered_username}'")
        if target_account:
            SystemAdmin.db.update_table("User", "active = 1", f"username = '{entered_username}'")
            return True
        else:
            return False