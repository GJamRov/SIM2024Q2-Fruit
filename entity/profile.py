import database

class userProfile:

    #Static Variable
    user_db = database.Database("SampleDatabase")
    profile_db =  database.Database("ProfileDatabase")

    def __init__(self, username, name, type, desc):
        self.username = username
        self.name = name
        self.type = type
        self.desc = desc
    
    #TODO: 8. Create user profiles
    def create_profile(self):
        pass

    #TODO: 9. View user profiles
    def view_profile(self, db_connection):
        pass

    #TODO: 10. Update user profile
    def update_profile(self):
        pass

    #TODO: 11. Suspend user profile
    def suspend_profile(self, db_connection):
        pass

    #TODO: 12. Search user profile
    def search_profile(self, db_connection):
        pass    