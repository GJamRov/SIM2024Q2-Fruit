from entity.rea import REA

class createPLController:

    def __init__(self):
        pass

    def createPropertyListing(self, agentName, propertyDetails:list) -> bool:
        found_rea = REA.db.search_one("User", f"username = '{agentName}'")
        if found_rea:
            found_rea = found_rea[:4] + found_rea[5:]
            tREA = REA(*found_rea)
            return tREA.createListing(propertyDetails)
        else:
            return False
        