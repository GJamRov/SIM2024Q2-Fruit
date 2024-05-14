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
        
        

        """
        #Length of tuple
        length_tuple = len(review_tuples)

        total_rating = 0
        #Iterate to add the total rating
        for i in range(length_tuple):
            current_tuple = review_tuples[i]
            current_rating = current_tuple[1]
            total_rating += current_rating
        
        #Calculate average rating
        average_rating = total_rating / length_tuple

        return average_rating
        """

    #Edit rating
    def editRating(self, new_rating, user_id, agent_id, role):
        Rating.connect_database("SampleDatabase")
        #Check if user previously has existing rating with selected agent
        rating_tuples = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
        length_tuple = len(rating_tuples)
        hasRating = False
        old_rating_index = 0
        old_rating = 0
        
        """
        #If user has not made any rating
        if(length_tuple == 0):
            return False
        else:
            for i in range(length_tuple):
                current_tuple = rating_tuples[i]
                current_agent = current_tuple[3]

                if(current_agent == agent_id):
                    hasRating = True
                    old_rating_index = i
                    old_rating = current_tuple[1]

            if(hasRating == False):
                return False
            else:
                #Delete from table the old rating
                Rating.db.delete_from_table("Rating", f"rating = {old_rating}, userName = '{user_id}', userNameREA = '{agent_id}'")

                #Insert new rating
                Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")
                return True
        """
        Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}', {role}")
        rating_tuples = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
        
        for current_rating in rating_tuples:
            if current_rating[1] == new_rating and current_rating[3] == agent_id:
                return True
        
        return False



    #Create rating
    def giveRating(self, new_rating, user_id, agent_id, role, new_review):
        Rating.connect_database("SampleDatabase")
        rating_tuples = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
        
        Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}', {role}, '{new_review}'")
        rating_tuples2 = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
        
        if(len(rating_tuples2) > len(rating_tuples)):
            return True
        else:
            return False