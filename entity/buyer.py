from entity.user import User

class Buyer(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, 3, active)
    
    def viewListing(self, search_param = "") -> list:
        """View Listing by serach_param"""
        if search_param == "": # 28. View each property listings
            search_result = Buyer.db.view_table("Property")
            return list(search_result)

        else: # View by ID
            search_param =  f"id ='{search_param}'"
            search_result = Buyer.db.search_one("Property", search_param=search_param)
            self.updateViewCount(search_result)
            return list(search_result)

    def updateViewCount(self, pl):
        """ Increments the view count of a property by one when selected """
        p_id = pl[0]
        updated_p_view_count = pl[-2] + 1
        Buyer.db.update_table("Property", f"view_count = {updated_p_view_count}", f"id = {p_id}")

    # 30. View propety listings in favourite list
    def view_favourites(self):
        """ Returns buyer's wishlisted properties """
        buyer_fav = Buyer.db.join_prop_fav(self.get_id())
        return list(buyer_fav)

    # 31. Save property listings to favourite list
    def add_favourite(self, pl_id):
        """ Adds a new property to buyer's wishlist """
        fav_entry = Buyer.db.search_one("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
        curr_PL = Buyer.db.search_one("Property", f"id = {pl_id}")
        if fav_entry: # If property listing exists -> Has been favourited
            return False
        else: 
            print(curr_PL)
            # Add new property to Favourite table
            Buyer.db.insert_into_table("Favourite", f"NULL, {self.get_id()}, {pl_id}")
            # Update property listing's wishlist count
            new_wishlist_count = curr_PL[-1] + 1
            Buyer.db.update_table("Property", f"wishlisted = {new_wishlist_count}", f"id = {curr_PL[0]}")
            return True
    
    # Remove property listings from favourite list
    def remove_favourite(self, pl_id):
        fav_entry = Buyer.db.search_one("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
        curr_PL = Buyer.db.search_one("Property", f"id = {pl_id}")
        if fav_entry: # If property listing exists in Favourite table -> Has been favourtied
            # Delete property from Favourite table
            Buyer.db.delete_from_table("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
            # Update property listing's wishlist count
            new_wishlist_count = curr_PL[-1] - 1
            Buyer.db.update_table("Property", f"wishlisted = {new_wishlist_count}", f"id = {curr_PL[0]}")
            return True
        else:
            return False

    def get_agent(self, rea_id):
        """ Returns agent object with matching name """
        agent = Buyer.db.search_one("User", f"id = '{rea_id}'")
        return agent

    def buy_property(self, listing_id):
        """ Buys a property and updates the property's status """
        found_property = Buyer.db.search_one("Property", f"id = {listing_id}")
        if found_property:
            Buyer.db.update_table("Property", f"buyer_id = {self.get_id()}", f"id = {listing_id}")
            return True
        else:
            return False