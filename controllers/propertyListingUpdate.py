from entity.user import User
from entity.rea import REA

class updatePLController:

    def __init__(self):
        pass

    def getOneSeller(self, seller_id):
        seller = REA.db.search_one("User", f"id = {seller_id}")
        return seller