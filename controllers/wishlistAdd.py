from entity.user import User
from entity.buyer import Buyer

class addToFavouritesController:

    def __init__(self):
        pass
    
    def addToFavourites(self, username, property_id) -> bool:
        """Adds a property to user's wishlist"""
        found_user = User.db.search_one("User", f"username = '{username}'")
        if found_user:
            role = found_user[4]
            found_user = found_user[:4] + found_user[5:]
            favs = []

            if role == 3: # Buyer has favourites
                t_Buyer = Buyer(*found_user)
                return t_Buyer.add_favourite(property_id)

            else:
                return False

        else:
            return False