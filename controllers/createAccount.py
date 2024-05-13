from entity.admin import SystemAdmin

class createAccountController:

    def __init__(self) -> None:
        pass

    def addUserAccount(self, newAccDetails) -> bool:
        return SystemAdmin.addUserAccount(newAccDetails)