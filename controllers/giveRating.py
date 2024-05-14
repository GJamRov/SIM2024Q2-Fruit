from entity.rating import Rating

class giveRatingController:
  def __init__(self) -> None:
    pass

  def giveRating(self, new_rating, user_id, agent_id, role, new_review):
    successBool = Rating.giveRating(self, new_rating, user_id, agent_id, role, new_review)
    return successBool