from database import Database

class Rating:
    db = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def connect_database(db_name):
        if not Rating.db:
            Rating.db = Database(db_name)

    # 19. View my ratings
    def viewRating(self, agent_id, role):
        Rating.connect_database("SampleDatabase")
        #Get the rating tuples where userNameREA == agent_id
        if(role == 2):
            review_tuples = Rating.db.search_by_keyword("Rating", agent_id, ["userNameREA"])
            return review_tuples
        else:
            review_tuples = Rating.db.search_by_keyword("Rating", agent_id, ["userName"])
            return review_tuples

    #Edit rating
    def editRating(self, review_id, new_rating, user_id, role, new_review):
        Rating.connect_database("SampleDatabase")
        
        #Get the tuples of the old review
        old_review_tuples = Rating.db.search_by_keyword("Review", new_review, ["review"])
        review_index = 0
        
        for review in old_review_tuples:
            if review[2] == user_id and review[0] == review_id:
                review_index = review[0]

        old_rating_tuple = Rating.db.search_by_keyword("Rating", review_index, ["review_id"])
        
        for rating in old_rating_tuple:
            if rating[5] == review_id and rating[2] == user_id:
                Rating.db.update_table("Rating", f"rating = {new_rating}", f"review_id = {review_index}")
                return True
            else:
                return False

    #Create rating
    def giveRating(self, new_rating, user_id, agent_id, role, new_review):
        Rating.connect_database("SampleDatabase")
        rating_tuples = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
        review_tuples = Rating.db.search_by_keyword("Review", new_review, ["review"])
        agent_tuples = Rating.db.search_by_keyword("User", 2, ["role"])
        review_index = 0
        isREA = False

        for agent in agent_tuples:
            if agent[1] == agent_id:
                isREA = True

        for review in review_tuples:
            if review[2] == user_id and review[3] == agent_id:
                review_index = review[0]

        if(isREA == True):
            Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}', {role}, {review_index}")
            return True
        else:
            return False
        
    def returnRatingTable(self):
        Rating.connect_database("SampleDatabase")

        return Rating.db.view_table("Rating")