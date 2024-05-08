from entity.admin import SystemAdmin

class suspendAccountCtl:

    def __init__():
        pass

    def viewUserAccount(self, adminName, userDetails):
        """Suspends User Account"""
        found_admin = SystemAdmin.db.search_one("User", f"username = '{adminName}'")
        # Check if adminName is valid
        if found_admin:
            t_admin = SystemAdmin(*found_admin)
            t_admin.suspend_account(userDetails)
            return True
        else:
            return False