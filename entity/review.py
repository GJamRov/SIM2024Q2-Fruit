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
        hasReview = False

        check_for_review = Review.db.search_by_keyword("Review", user_id, ["userName"])
        """ 
        #Checks if user has given a review to REA 
        for i in range(tuple_length):
            current_tuple = check_for_review[i]

            if((current_tuple[2] == user_id) and (current_tuple[3] == agent_id)):
                hasReview = True

        #If user has already given a review, cannot give review again
        if(hasReview == True):
            return False

        #If user has not given a review to this REA
        else:
            Review.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}'")
            return True
        """
        Review.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}', {role}")

        check_for_review2 = Review.db.search_by_keyword("Review", user_id, ["userName"])

        if(len(check_for_review2) > len(check_for_review)):
            return True
        else:
            return False

    # Edit reviews
    # Assuming the user already has made a review previously to specified agent
    def editReview(self, review_id, new_review, user_id, role):
        Review.connect_database("SampleDatabase")
        
        #Get the tuples of the old review
        #old_review_tuples = Review.db.search_by_keyword("Review", review_id, ["id"])
        #old_review = old_review_tuples[1]

        """
        if old_review_tuples:
            Review.db.update_table("Review", f"review = '{new_review}'", f"id = {review_id}")
            return True
        else:
            return False
        """
        Review.db.update_table("Review", f"review = '{new_review}'", f"id = {review_id}")
        review_tuple = Review.db.search_by_keyword("Review", review_id, ["id"])

        for review in review_tuple:
            if review[1] == new_review and review[0] == review_id:
                return True
            else:
                return False

        """
        new_review_tuples = Review.db.search_by_keyword("Review", review_id, ["id"])
        new_review_view = new_review_tuples[1]

        if old_review == new_review_view:
            return False
        else:
            return True
        """