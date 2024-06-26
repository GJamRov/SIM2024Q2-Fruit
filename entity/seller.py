from entity.user import User

class Seller(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, 4, active)

    def viewListing(self, search_param = "") -> list:
        """View Listing by serach_param"""
        if search_param == "":
            search_result = Seller.db.view_table("Property")
            return list(search_result)
        
        elif search_param == "profile": # For MY PROFILE tab
            search_result = Seller.db.search_by_keyword("Property", self.get_id(), ["seller_id"])
            return list(search_result)

        else: # View by ID
            search_param =  f"id ='{search_param}'"
            search_result = Seller.db.search_one("Property", search_param=search_param)
            return list(search_result)

    # 42. View property listing views
    def view_PL_views(self, pl_name):
        """Returns one PL's view"""
        # INSERT INTO Property VALUES(NULL, 'property 100', 'West Coast', 'Charming 4-bedroom cottage nestled in the countryside, surrounded by lush greenery and scenic views.', '3.png', 870919, 74, 55, -1, 3630, 7812)
        curr_pl = Seller.db.search_one("Property", f"name = {pl_name}")
        if curr_pl:
            return int(curr_pl[-2])
        else:
            return -1
        

    # 43. View propety listing saves
    def view_PL_saves(self, pl_name):
        """Returns one PL's wishlisted"""
        # INSERT INTO Property VALUES(NULL, 'property 100', 'West Coast', 'Charming 4-bedroom cottage nestled in the countryside, surrounded by lush greenery and scenic views.', '3.png', 870919, 74, 55, -1, 3630, 7812)
        curr_pl = Seller.db.search_one("Property", f"name = {pl_name}")
        if curr_pl:
            return int(curr_pl[-1])
        else:
            return -1
    