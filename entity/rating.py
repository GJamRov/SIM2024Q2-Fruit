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
  def viewRating(self, agent_id):
      Rating.connect_database("SampleDatabase")
      #Get the rating tuples where userNameREA == agent_id
      review_tuples = Rating.db.search_by_keyword("Rating", agent_id, ["userNameREA"])

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
  def editRating(self, new_rating, user_id, agent_id):
      Rating.connect_database("SampleDatabase")
      #Check if user previously has existing rating with selected agent
      rating_tuples = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
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
              Rating.db.delete_from_table("Rating", f"rating = {old_rating}, userName = '{user_id}', userNameREA = '{agent_id}'")

              #Insert new rating
              Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")
              return True


  #Create rating
  def giveRating(self, new_rating, user_id, agent_id):
      Rating.connect_database("SampleDatabase")
      rating_tuple = Rating.db.search_by_keyword("Rating", user_id, ["userName"])
      length_tuple = len(rating_tuple)
      hasRating = False

      if(length_tuple == 0):
          #Insert new rating
          Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")

      else:
          for i in range(length_tuple):
              current_tuple = rating_tuple[i]
              current_agent= current_tuple[3]

              if(current_agent == agent_id):
                  hasRating = True

          
          if(hasRating == True):
              return False
          else:
              Rating.db.insert_into_table("Rating", f"NULL, {new_rating}, '{user_id}', '{agent_id}'")
              return True