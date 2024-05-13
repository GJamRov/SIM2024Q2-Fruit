from entity.admin import SystemAdmin

class reactivateUserAccountController:

    def __init__(self):
        pass

    def reactivateUserAccount(self, profile) -> bool:        
        return SystemAdmin.reactivate_account(profile)
