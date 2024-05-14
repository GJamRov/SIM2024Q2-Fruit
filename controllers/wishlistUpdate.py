from entity.user import User
from entity.buyer import Buyer

class updateFavouritesController:

    def __init__(self):
        pass

    def updateFavouritesTable(self, username, property_id) -> bool:
        found_user = User.db.search_one("User", f"username = '{username}'")
        if found_user and found_user[4] == 3:
            found_user = found_user[:4] + found_user[5:]
            t_buyer = Buyer(*found_user)
             # Check if property_id and found_user is found in Favourite table
            if User.db.search_one("Favourite", f"user_id = '{found_user[0]}' AND property_id = {property_id}"): # If exists, remove
                print("FAVOURITE REMOVING")
                return t_buyer.remove_favourite(property_id)
            
            else: #If dont exist, add
                return t_buyer.add_favourite(property_id)
        else:
            return False
    