from entity.admin import SystemAdmin

class updateAccountCtl:

    def __init__():
        pass

    def viewUserAccount(self, adminName, newUserDetails):
        found_admin = SystemAdmin.db.search_one("User", f"username = '{adminName}'")
        # Check if adminName is valid
        if found_admin:
            t_admin = SystemAdmin(*found_admin)
            t_admin.update_account(newUserDetails)
            return True
        else:
            return False
