from entity.profile import userProfile

class createUserProfileController:

    def __init__(self):
        pass

    def createUserProfile(self, UP) -> bool:
        return userProfile.create_profile(UP)