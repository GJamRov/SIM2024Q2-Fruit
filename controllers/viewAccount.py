from entity.admin import SystemAdmin

class viewAccountCtl:

    def __init__(self):
        pass

    def viewUserAccount(self, adminName, userDetails) -> bool:
        found_admin = SystemAdmin.db.search_one("User", f"username = '{adminName}'")
        # Check if adminName is valid
        if found_admin:
            t_admin = SystemAdmin(*found_admin)
            t_admin.view_account(userDetails)
            return True
        else:
            return False
        
    def viewAllUsers(self):
        return SystemAdmin.view_all_user()
