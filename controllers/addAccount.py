from entity.admin import SystemAdmin

class addAccountCtl:

    def __init__(self) -> None:
        pass

    def addUserAccount(self, adminName, newAccDetails) -> bool:
        found_admin = SystemAdmin.db.search_one("User", f"username = '{adminName}'")
        # Check if adminName is valid
        if found_admin:
            t_admin = SystemAdmin(*found_admin)
            t_admin.addUserAccount(newAccDetails)
            return True
        else:
            return False
