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
  def viewReview(self, agent_id):
      Review.connect_database("SampleDatabase")
      #Get the whole review tuples where userNameREA = agent_id
      review_tuples = Review.db.search_by_keyword("Review", agent_id, ["userNameREA"])
      return review_tuples
    
  # Create reviews
  def giveReview(self, new_review, agent_id, user_id):
      Review.connect_database("SampleDatabase")
      hasReview = False

      check_for_review = Review.db.search_by_keyword("Review", user_id, ["userName"])

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
          Review.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}'")
          return True

  # Edit reviews
  # Assuming the user already has made a review previously to specified agent
  def editReview(self, new_review, old_review, agent_id, user_id):
      Review.connect_database("SampleDatabase")
      hasReview = False
      old_review_index = 0

      #Get the tuples of the old review
      old_review_tuples = Review.db.search_by_keyword("Review", user_id, ["userName"])

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

          Review.db.delete_from_table("Review", f"review = '{old_review}', userName = '{user_id}', userNameREA = '{agent_id}'")

          Review.db.insert_into_table("Review", f"NULL, '{new_review}', '{user_id}', '{agent_id}'")
          return True