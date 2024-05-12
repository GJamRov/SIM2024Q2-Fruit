from entity.user import User
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

class viewPLController:

    def __init__(self):
        pass

    def viewListing(self, userName, propertyDetail='', sortOrder = ''):
        found_user = User.db.search_one("User", f"username = '{userName}'")
        # print(propertyDetail)
        # Check if adminName is valid
        if found_user:
            print(found_user)
            role = found_user[4]
            found_user = found_user[:4] + found_user[5:]
            print(found_user)
            properties = []
            if role == 2:
                tREA = REA(*found_user)
                properties = tREA.viewListing(propertyDetail)
            elif role == 3:
                tBuyer = Buyer(*found_user)
                properties = tBuyer.viewListing(propertyDetail)
            elif role == 4:
                tSeller = Seller(*found_user)
                properties = tSeller.viewListing(propertyDetail)
            # print("Properties before sorting:", properties[:5])  # Debug statement
            # print(properties[0], "I AM HERE")
            if sortOrder == 'asc':
                # print(sortOrder)
                properties.sort(key=lambda x: x[5])
            elif sortOrder == 'desc':
                # print(sortOrder)
                properties.sort(key=lambda x: x[5], reverse=True)
            #print("Properties after sorting:", properties[:5])  # Debug statement
            return properties
        else:
            return []