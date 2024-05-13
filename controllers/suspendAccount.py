from entity.admin import SystemAdmin

class suspendAccountController:

    def __init__(self):
        pass

    def suspendUserAccount(self, account):
        return SystemAdmin.suspend_account(account)