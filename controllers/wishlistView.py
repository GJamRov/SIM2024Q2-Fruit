from entity.user import User
from entity.buyer import Buyer

class viewFavouritesController:

    def __init__(self):
        pass
    
    def viewFavourites(self, username, sortOrder = ""):
        """Returns a list of favourited properties by the user"""
        found_user = User.db.search_one("User", f"username = '{username}'")
        if found_user:
            role = found_user[4]
            found_user = found_user[:4] + found_user[5:]
            favs = []

            if role == 3: # Buyer has favourites
                t_Buyer = Buyer(*found_user)
                favs = t_Buyer.view_favourites()

            # Sorts properties in ascending or descedning offer if sortOrder is specified
            if sortOrder == 'asc':
                favs.sort(key=lambda x: x[5])

            elif sortOrder == 'desc':
                favs.sort(key=lambda x: x[5], reverse=True)

            return favs

        else:
            return []