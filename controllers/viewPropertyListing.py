from entity.user import User
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

class viewPLController:

    def __init__(self):
        pass

    def viewListing(self, userName, propertyDetail='', sortOrder = ''):
        found_user = User.db.search_one("User", f"username = '{userName}'")
        # Check if userName belongs to an existing user
        if found_user:
            role = found_user[4]
            found_user = found_user[:4] + found_user[5:]
            properties = []
            
            ## REA
            if role == 2:
                tREA = REA(*found_user)
                properties = tREA.viewListing(propertyDetail)

            ## Buyer
            elif role == 3 and propertyDetail == 'profile':
                tBuyer = Buyer(*found_user)
                properties = tBuyer.view_favourites()
                
            elif role == 3:
                tBuyer = Buyer(*found_user)
                properties = tBuyer.viewListing(propertyDetail)

            ## Seller
            elif role == 4:
                tSeller = Seller(*found_user)
                properties = tSeller.viewListing(propertyDetail)

            # Sorts properties in ascending or descedning offer if sortOrder is specified
            if sortOrder == 'asc':
                properties.sort(key=lambda x: x[5])

            elif sortOrder == 'desc':
                properties.sort(key=lambda x: x[5], reverse=True)

            return properties
        
        else:
            return []
        
    def getOneListing(self, p_id):
        prop = User.db.search_one("Property", f"id = {p_id}")
        return prop
    
    def getAgent(self, userName, rea_id):
        found_user = User.db.search_one("User", f"username = '{userName}'")
        # Check if userName belongs to an existing user
        if found_user:
            role = found_user[4]
            found_user = found_user[:4] + found_user[5:]
            # Checks that user is an REA, buyer or seller
            if role == 3 or role == 2:
                tBuyer = Buyer(*found_user)
                found_rea = tBuyer.get_agent(rea_id)
                return found_rea
        
        else:
            return None
        

    def getRating(self, rea):
        if type(rea) == tuple:
            details = rea[:4] + rea[5:]
            tREA = REA(*details)
            return tREA.get_rating()
        elif type(rea) == str:
            found_rea = User.db.search_one("User", f"username='{rea}'")
            details = found_rea[:4] + found_rea[5:]
            tREA = REA(*details)
            return tREA.get_rating()
    
    def getReview(self, rea):
        if type(rea) == tuple:
            details = rea[:4] + rea[5:]
            tREA = REA(*details)
            return tREA.get_reviews()
        elif type(rea) == str:
            found_rea = User.db.search_one("User", f"username='{rea}'")
            details = found_rea[:4] + found_rea[5:]
            tREA = REA(*details)
            return tREA.get_reviews()