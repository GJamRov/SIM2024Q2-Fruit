from entity.user import User
from entity.rea import REA
from entity.buyer import Buyer
from entity.seller import Seller

class viewPLController:

    def __init__(self):
        pass

    def viewListing(self, userName, propertyDetail):
        found_user = User.db.search_one("User", f"username = '{userName}'")
        # print(found_user)
        # Check if adminName is valid
        if found_user:
            id = found_user[0]
            name = found_user[1]
            password = found_user[2]
            email = found_user[3]
            role = found_user[4]
            active = found_user[5]
            #print(id, name, password, email, role, active)
            properties = []
            if role == 2:
                tREA = REA(id, name, password, email, active)
                properties = tREA.viewListing(propertyDetail)
            elif role == 3:
                tBuyer = Buyer(id, name, password, email, active)
                properties = tBuyer.viewListing(propertyDetail)
            elif role == 4:
                tSeller = Seller(id, name, password, email, active)
                properties = tSeller.viewListing(propertyDetail)

        return properties