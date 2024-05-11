from entity.user import User

class REA(User):

    def __init__(self, userID, username, password, email, active):
        super().__init__(userID, username, password, email, active)
    
    # 15. Create new property listings
    def createListing(self, newPropertyDetails):
        
        # If property details already exist in database
        if ():
            pass

        else:
            # f"NULL, '{p_name}', {price}, {view_count}, {wishlisted}"
            details = f"NULL, '{newPropertyDetails[0]}', {newPropertyDetails[1]}, 0, 0"
            REA.db.insert_into_table("Property", details)
            return True

    # 16. View existing property listings
    def view_listing(self, p_name = ""):
        if p_name == "": # View all accounts
            search_result = REA.db.view_table("Property")
            return list(search_result)
        else:
            search_param =  f"p_name ='{p_name}'"
            search_result = REA.db.search_one("Property", search_param=search_param)
            return list(search_result)

    # 17. Update property listings
    def update_listing(self, entered_details):
        target_property = REA.db.search_one("Property", f"p_name = '{entered_details[0]}'")
        if target_property:
            update_details = ""
            # Update target_account with remaining information
            REA.db.update_table("Property", update_details, f"p_name = '{entered_details[0]}'")
            return True
        else:
            return False

    # 18. Delete property listings
    def delete_listing(self, p_id):
        """Delete property listing"""
        target_property  = REA.db.search_one("Property", f"p_id = {p_id}")
        if target_property:
            REA.db.delete_from_table("Property", f"p_id = {p_id}")
            return True
        else:
            return False

    # 19. View my ratings
    def viewRating(self, agent_id):
        #Get the rating tuples where userNameREA == agent_id
        review_tuples = REA.db.search_by_keyword("Rating", agent_id, ["userNameREA"])

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
    
    #Edit rating
    def editRating(self, new_rating, user_id, agent_id):
        #Check if user previously has existing rating with selected agent
        rating_tuples = REA.db.search_by_keyword("Rating", user_id, ["userName"])
        length_tuple = len(rating_tuples)
        hasRating = False
        old_rating_index = 0
        old_rating = 0
        
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
                REA.db.delete_from_table("Rating", f"rating = {old_rating}, userName = '{user_id}', userNameREA = '{agent_id}'")

                #Insert new rating
                REA.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")
                return True


    #Create rating
    def giveRating(self, new_rating, user_id, agent_id):
        rating_tuple = REA.db.search_by_keyword("Rating", user_id, ["userName"])
        length_tuple = len(rating_tuple)
        hasRating = False

        if(length_tuple == 0):
            #Insert new rating
            REA.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")

        else:
            for i in range(length_tuple):
                current_tuple = rating_tuple[i]
                current_agent= current_tuple[3]

                if(current_agent == agent_id):
                    hasRating = True

            
            if(hasRating == True):
                return False
            else:
                REA.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")
                return True


    # 20. View my reviews
    def viewReview(self, agent_id):
        #Get the whole review tuples where userNameREA = agent_id
        review_tuples = REA.db.search_by_keyword("Review", agent_id, ["userNameREA"])
        return review_tuples
    
    # Create reviews
    def giveReview(self, new_review, agent_id, user_id):
        hasReview = False

        check_for_review = REA.db.search_by_keyword("Review", user_id, ["userName"])

        tuple_length = len(check_for_review)

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
            REA.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}'")
            return True

    # Edit reviews
    # Assuming the user already has made a review previously to specified agent
    def editReview(self, new_review, old_review, agent_id, user_id):
        hasReview = False
        old_review_index = 0

        #Get the tuples of the old review
        old_review_tuples = REA.db.search_by_keyword("Review", user_id, ["userName"])

        #Length of tuple
        tuple_length = len(old_review_tuples)

        for i in range(tuple_length):
            current_tuple = old_review_tuples[i]
            current_review = current_tuple[1]
            current_agent_id = current_tuple[3]

            if(current_agent_id == agent_id):
                old_review_index = i
                hasReview = True

        if(hasReview != True):
            return False
        
        else:

            #Remove the tuple of the old review
            """
            tuple_to_remove = (old_review_index, old_review, user_id, agent_id)

            new_tuple = tuple(inner_tuple for inner_tuple in old_review_tuples if inner_tuple != tuple_to_remove)

            REA.db.delete_from_table("Review", f"review = '{old_review}'")

            for j in range(tuple_length - 1):
                current_tuple = new_tuple[j]
                current_review = current_tuple[1]
                current_user_id = current_tuple[2]
                current_agent_id = current_tuple[3]

                REA.db.insert_into_table("Review", f"NULL, '{current_review}', '{current_user_id}', '{current_agent_id}'")
            """

            REA.db.delete_from_table("Review", f"review = '{old_review}', userName = '{user_id}', userNameREA = '{agent_id}'")

            REA.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}'")
            return True
