from entity.user import User
from entity.rea import REA

class updatePLController:

    def __init__(self):
        pass

    def getOneSeller(self, seller_id):
        seller = REA.db.search_one("User", f"id = {seller_id}")
        return seller
    
    def update_listing(self, agentName, newDetails):
        found_rea = REA.db.search_one("User", f"username = '{agentName}'")
        if found_rea:
            found_rea = found_rea[:4] + found_rea[5:]
            tREA = REA(*found_rea)
            # print("UPDATING: IN PROGRESS")
            return tREA.update_listing(newDetails)
        else:
            return False