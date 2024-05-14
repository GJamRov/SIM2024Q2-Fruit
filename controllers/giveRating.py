from entity.rating import Rating

class giveRatingController:
  def __init__(self) -> None:
    pass

  def giveRating(self, review_id, new_rating, user_id, role, new_review):
    successBool = Rating.giveRating(self, review_id, new_rating, user_id, role, new_review)
    return successBool