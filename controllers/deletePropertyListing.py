from entity.rea import REA

class deletePLController:

    def __init__(self):
        pass

    def delete_listing(self, username, p_id):
        found_rea = REA.db.search_one("User", f"username = '{username}'")
        if found_rea:
            found_rea = found_rea[:4] + found_rea[5:]
            tREA = REA(*found_rea)
            # print("STRING", type(p_id))
            return tREA.delete_listing(p_id=p_id)
        else:
            return True