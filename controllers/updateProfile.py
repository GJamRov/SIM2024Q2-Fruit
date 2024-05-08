from entity.profile import userProfile

class updateUserProfileController:

    def __init__(self):
        pass

    def updateUserProfile(self, profile, entered_desc) -> bool:
        return userProfile.update_profile(profile, entered_desc)