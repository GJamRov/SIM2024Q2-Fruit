from entity.rea import REA

class createPLController:

    def __init__(self):
        pass

    def createPropertyListing(self, agentName, propertyDetails:list) -> bool:
        found_rea = REA.db.search_one("User", f"username = '{agentName}'")
        if found_rea:
            tREA = REA(*found_rea)
            return tREA.createListing(propertyDetails)
        else:
            return False
        