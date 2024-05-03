from myproj.test.user import User

# System Admins Class inherits from User Class


class SystemAdmin(User):

    def __init__(self, userID, username, password, email):
        super().__init__(userID, username, password, email)

    # TODO: 3. Create user accounts
    def create_account(self):
        pass

    # TODO: 4. View user accounts
    def view_account(self):
        pass

    # TODO: 5. Update user accounts
    def update_account(self):
        pass

    # TODO: 6. Suspend user account
    def suspend_account(self):
        pass

    # TODO: 8. Create user profiles
    def create_profile(self):
        pass

    # TODO: 9. View user profiles
    def view_profile(self):
        pass

    # TODO: 11. Suspend user profile
    def suspend_profile(self):
        pass

    # TODO: 12. Search user profile
    def search_profile(self):
        pass
