from entity.profile import userProfile

class reactivateUserProfileController:

    def __init__(self):
        pass

    def reactivateUserProfile(self, profile) -> bool:        
        return userProfile.reactivate_profile(profile)