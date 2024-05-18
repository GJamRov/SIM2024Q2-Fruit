from entity.admin import SystemAdmin

class viewAccountController:

    def __init__(self):
        pass

    def viewUserAccount(self, account) -> bool:
        return SystemAdmin.view_account(account)
        
    def viewAllUsers(self):
        return SystemAdmin.view_all_user()
    
    def viewAllREA(self):
        REAs =  SystemAdmin.db.search_by_keyword("User", "2", ['role'])
        return REAs