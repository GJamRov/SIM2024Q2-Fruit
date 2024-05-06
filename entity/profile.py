from database import Database

class userProfile:

    #Static Variable
    db = None

    def __init__(self, type, desc):
        self.type = type
        self.desc = desc

    @staticmethod
    def connect_database(db_name):
        if not userProfile.db:
            userProfile.db = Database(db_name)
    
    #TODO: 8. Create user profiles
    def create_profile(self, UP) -> bool:
        profile_data = userProfile.db.search_one("Profile", f"type = '{UP[0]}'")
        
        if not profile_data:
            profile = f"NULL, '{UP[0]}', '{UP[1]}'"
            userProfile.db.insert_into_table("Profile", profile)
            return True
        if profile_data:
            return False

    #TODO: 9. View user profiles
    def view_profile(self, profile):
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")
        
        if profile_data:
            self = userProfile(*profile_data)
            if profile == self.type:
                return profile_data

    #TODO: 10. Update user profile
    def update_profile(self, profile, entered_desc):
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")
        
        if profile_data:
            userProfile.db.update_table("Profile", f"desc = {entered_desc}", f"type = {profile}")
            return True
        if not profile_data:
            return False

    #TODO: 11. Suspend user profile
    def suspend_profile(self, profile) -> bool:
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")
        
        if profile_data:
            userProfile.db.delete_from_table("Profile", f"type = '{profile}")
            return True
        if not profile_data:
            return False        

    #TODO: 12. Search user profile
    def search_profile(self, username):
        profile_data = userProfile.db.search_by_keyword("Profile", username, ["type", "desc"])
        return profile_data