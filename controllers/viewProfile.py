from entity.profile import userProfile

class viewUserProfileController:

    def __init__(self):
        pass

    def viewUserProfile(self, profile):
        return userProfile.view_profile(profile)
    
    def viewAllUserProfile(self):
        return userProfile.view_all_profile()