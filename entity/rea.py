from entity.user import User

class REA(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)
    
    # 15. Create new property listings
    def createListing(self, newPropertyDetails):
        
        # If property details already exist in database
        if ():
            pass

        else:
            # f"NULL, '{p_name}', {price}, {view_count}, {wishlisted}"
            details = f"NULL, '{newPropertyDetails[0]}', {newPropertyDetails[1]}, 0, 0"
            REA.db.insert_into_table("Property", details)
            return True

    # 16. View existing property listings
    def view_listing(self, p_name = ""):
        if p_name == "": # View all accounts
            search_result = REA.db.view_table("Property")
            return list(search_result)
        else:
            search_param =  f"p_name ='{p_name}'"
            search_result = REA.db.search_one("Property", search_param=search_param)
            return list(search_result)

    # 17. Update property listings
    def update_listing(self, entered_details):
        target_property = REA.db.search_one("Property", f"p_name = '{entered_details[0]}'")
        if target_property:
            update_details = ""
            # Update target_account with remaining information
            REA.db.update_table("Property", update_details, f"p_name = '{entered_details[0]}'")
            return True
        else:
            return False

    # 18. Delete property listings
    def delete_listing(self, p_id):
        """Delete property listing"""
        target_property  = REA.db.search_one("Property", f"p_id = {p_id}")
        if target_property:
            REA.db.delete_from_table("Property", f"p_id = {p_id}")
            return True
        else:
            return False

    # 19. View my ratings

    # 20. View my reviews
