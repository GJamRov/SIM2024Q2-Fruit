from entity.user import User

class REA(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, 2, active)
    
    # 15. Create new property listings
    def createListing(self, newPropertyDetails):
        """Inserts a property listing into database"""
        if not newPropertyDetails or len(newPropertyDetails) != 6:
            return False  # Input validation failed
        try:
            # f"NULL, '{p_name}', '{location}', '{description}', '{img_name}', {price}, {rea_id}, {seller_id}, {sold_buyer}, {view_count}, {wishlisted}"
            # Sample newPropertyDetails: [name, location, image_filename, price, description, seller]
            seller_id = User.db.search_one("User", f"username = '{newPropertyDetails[5]}'")[0]
            details = f"NULL, '{newPropertyDetails[0]}', '{newPropertyDetails[1]}', '{newPropertyDetails[4]}', '{newPropertyDetails[2]}', {newPropertyDetails[3]}, {self.get_id()}, {seller_id}, -1, 0, 0"
            REA.db.insert_into_table("Property", details)
            return True

        except Exception as e:
            print(f"Error creating listing: {e}")
            return False

    # 16. View existing property listings
    def viewListing(self, search_param = "", cols=[]) -> list:
        """View Listing by ID"""
        if search_param == "": # View all accounts
            search_result = REA.db.view_table("Property")
            return list(search_result)
        
        elif search_param == "profile": # For MY PROFILE tab
            search_result = REA.db.search_by_keyword("Property", self.get_id(), ["rea_id"])
            return list(search_result)

        else: # View by ID
            search_param =  f"id ='{search_param}'"
            search_result = REA.db.search_one("Property", search_param=search_param)
            return list(search_result)
        
    def updateViewCount(self, pl):
        """ Increments the view count of a property by one when selected """
        p_id = pl[0]
        updated_p_view_count = pl[-2] + 1
        REA.db.update_table("Property", f"view_count = {updated_p_view_count}", f"id = {p_id}")


    # 17. Update property listings
    def update_listing(self, entered_details:list):
        """Updates a property listing"""
        if not entered_details or len(entered_details) != 7:
            return False
        
        try:
            curr_property = REA.db.search_one("Property", f"id = {entered_details[0]}")
            # print(curr_property)
            # f"NULL, '{p_name}', '{location}', '{description}', '{img_name}', {price}, {rea_id}, {seller_id}, {sold_buyer}, {view_count}, {wishlisted}"
            """
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
                                "name TEXT",
                                "location TEXT",
                                "description TEXT",
                                "img TEXT",
                                "price INTEGER",
                                "rea_id INTEGER",
                                "seller_id INTEGER",
                                "buyer_id INTEGER",
                                "view_count INTEGER",
                                "wishlisted INTEGER"
            """
            # Sample entered_details: [id, name, location, image_filename, price, description, seller]
            seller_id = User.db.search_one("User", f"username = '{entered_details[6]}'")[0]
            update_params = ''
            # print("IMAGE SOURCE",entered_details[3])
            if entered_details[3] == '':
                update_params = f"name='{entered_details[1]}', location='{entered_details[2]}', description='{entered_details[5]}', img='{curr_property[4]}', price={entered_details[4]}, seller_id={seller_id}"
            else:
                update_params = f"name='{entered_details[1]}', location='{entered_details[2]}', description='{entered_details[5]}', img='{entered_details[3]}', price={entered_details[4]}, seller_id={seller_id}"
            # print("UPDATING WITH", update_params)
            REA.db.update_table("Property", update_params, f"id = {int(entered_details[0])}")
            return True

        except Exception as e:
            print(f"Error updating listing: {e}")
            return False

    # 18. Delete property listings
    def delete_listing(self, p_id):
        """Delete property listing"""
        target_property  = REA.db.search_one("Property", f"id = {p_id}")
        if target_property:
            REA.db.delete_from_table("Property", f"id = {p_id}")
            return True
        else:
            return False
        
    def viewREATable(self):
        rea_table = REA.db.search_by_keyword("User", 2, ["role"])
        return rea_table

    


    
