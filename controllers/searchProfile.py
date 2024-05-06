from entity.profile import userProfile

class searchUserProfileController:

    def __init__(self):
        pass

    def searchUserProfile(self, username):
        return userProfile.search_profile(username)