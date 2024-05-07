from database import Database

class userProfile:

    #Static Variable
    db = None

    def __init__(self, id, type, desc):
        self.id = id
        self.type = type
        self.desc = desc

    @staticmethod
    def connect_database(db_name):
        if not userProfile.db:
            userProfile.db = Database(db_name)
    
    # Return all user profiles to be displayed in user profile tab
    def view_all_profile():
        userProfile.connect_database("SampleDatabase")
        userProfile.db.cursor.execute("SELECT * FROM Profile")
        profiles = userProfile.db.cursor.fetchall()
        return profiles

    #TODO: 8. Create user profiles
    def create_profile(UP) -> bool:
        userProfile.connect_database("SampleDatabase")
        profile_data = userProfile.db.search_one("Profile", f"type = '{UP[0]}'")
        
        if not profile_data:
            if UP[0] == 'System Admin':
                profile = f"1, '{UP[0]}', '{UP[1]}'"
            elif UP[0] == 'Real Estate Agent':
                profile = f"2, '{UP[0]}', '{UP[1]}'"
            elif UP[0] == 'Buyer':
                profile = f"3, '{UP[0]}', '{UP[1]}'"
            elif UP[0] == 'Seller':
                profile = f"4, '{UP[0]}', '{UP[1]}'"
            userProfile.db.insert_into_table("Profile", profile)
            return True
        if profile_data:
            return False

    #TODO: 9. View user profiles
    def view_profile(profile):
        userProfile.connect_database("SampleDatabase")
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")
        
        if profile_data:
            self = userProfile(*profile_data)
            if profile == self.type:
                return profile_data

    #TODO: 10. Update user profile
    def update_profile(profile, entered_desc):
        userProfile.connect_database("SampleDatabase")
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")

        if profile_data:
            userProfile.db.update_table("Profile", f"description = '{entered_desc}'", f"type = '{profile}'")
            return True
        if not profile_data:
            return False

    #TODO: 11. Suspend user profile
    def suspend_profile(profile) -> bool:
        userProfile.connect_database("SampleDatabase")
        profile_data = userProfile.db.search_one("Profile", f"type = '{profile}'")
        
        if profile_data:
            userProfile.db.delete_from_table("Profile", f"type = '{profile}'")
            return True
        if not profile_data:
            return False        

    #TODO: 12. Search user profile
    def search_profile(self, username):
        profile_data = userProfile.db.search_by_keyword("Profile", username, ["type", "description"])
        return profile_data