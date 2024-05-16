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
            # Checks that user is an REA, buyer or seller
            if role == 2:
                tREA = REA(*found_user)
                properties = tREA.viewListing(propertyDetail)
            elif role == 3:
                tBuyer = Buyer(*found_user)
                properties = tBuyer.viewListing(propertyDetail)
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
            if role == 3:
                tBuyer = Buyer(*found_user)
                found_rea = tBuyer.get_agent(rea_id)
                return found_rea
            
            elif role == 2:
                tREA = REA(*found_user)
                return (tREA.get_rating(), len(tREA.get_reviews()))
        
        else:
            return None
        
    def getRating(self, rea):
        details = rea[:4] + rea[5:]
        tRea = REA(*details)
        return tRea.get_rating()