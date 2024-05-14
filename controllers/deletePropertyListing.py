from entity.rea import REA

class deletePLController:

    def __init__(self):
        pass

    def delete_listing(self, username, listing):
        found_rea = REA.db.search_one("User", f"username = '{username}'")
        if found_rea:
            pass
        else:
            pass