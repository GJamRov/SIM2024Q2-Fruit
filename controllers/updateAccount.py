from entity.admin import SystemAdmin

class updateAccountController:

    def __init__(self):
        pass

    def updateUserAccount(self, newUserDetails):
        return SystemAdmin.update_account(newUserDetails)
