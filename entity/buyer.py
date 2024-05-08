from entity.user import User

class Buyer(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)

    # 23. Give reviews on an agent

    # 24. Give ratings on an agent

    # 25. Edit ratings on an agent

    # 26. Edit reviews on an agent

    # 27. View ratings on an agent

    # 28. View each property listings
    def view_all_listing(self):
        search_result = Buyer.db.view_table("Property")
        return list(search_result)

    # 29. Search new property listing
    def searchProperty(self, keyWord:str):
        # Use keyword to search through property listing description
        search_result = Buyer.db.search_by_keyword("Property", keyWord, ["location", "description"])
        return list(search_result)

    # 30. View propety listings in favourite list
    def view_favourites(self):
        buyer_fav = Buyer.db.search_by_keyword("Favourite", self.get_id(), ["user_id"])
        return list[buyer_fav]

    # 31. Save property listings to favourite list
    def save_favourite(self, pl_id):
        curr_PL = Buyer.db.search_one("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
        if curr_PL:
            return False
        else:
            Buyer.db.insert_into_table("Favourite", [f"NULL, {self.get_id()}, {pl_id}"])
            return True
    
    def unfavourite(self, pl_id):
        curr_PL = Buyer.db.search_one("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
        if curr_PL:
            Buyer.db.insert_into_table("Favourite", f"user_id = {self.get_id()} AND property_id = {pl_id}")
            return True
        else:
            return False

    # 32. Calculate mortage of property
    def calc_mortage(self):
        pass

    