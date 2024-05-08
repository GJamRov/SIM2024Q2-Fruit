from entity.profile import userProfile

class suspendUserProfileController:

    def __init__(self):
        pass

    def suspendUserProfile(self, profile) -> bool:        
        return userProfile.suspend_profile(profile)