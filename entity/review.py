from database import Database

class Review:
    db = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def connect_database(db_name):
        if not Review.db:
            Review.db = Database(db_name)

    # 20. View my reviews
    def viewReview(self, agent_id, role):
        Review.connect_database("SampleDatabase")
        #Get the whole review tuples where userNameREA = agent_id
        if(role == 2):
            review_tuples = Review.db.search_by_keyword("Review", agent_id, ["userNameREA"])
            return review_tuples
        else:
            review_tuples = Review.db.search_by_keyword("Review", agent_id, ["userName"])
            return review_tuples
        
    # Create reviews
    def giveReview(self, new_review, agent_id, user_id, role):
        Review.connect_database("SampleDatabase")
        isREA = False

        check_for_review = Review.db.search_by_keyword("Review", user_id, ["userName"])
        agent_tuple = Review.db.search_by_keyword("User", 2, ["role"])

        for agent in agent_tuple:
            if agent[1] == agent_id:
                isREA = True

        if(isREA == True):
            Review.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}', {role}")
            return True
        else:
            return False

    # Edit reviews
    # Assuming the user already has made a review previously to specified agent
    def editReview(self, review_id, new_review, user_id, role):
        Review.connect_database("SampleDatabase")
        
        review_tuple = Review.db.search_by_keyword("Review", review_id, ["id"])

        for review in review_tuple:
            if review[0] == review_id and review[2] == user_id:
                Review.db.update_table("Review", f"review = '{new_review}'", f"id = {review_id}")
                return True
            else:
                return False