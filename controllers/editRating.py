from entity.rating import Rating

class editRatingController:
  def __init__(self) -> None:
    pass

  def editRating(self, review_id, new_rating, user_id, current_role, new_review):
    successBool = Rating.editRating(self, int(review_id), new_rating, user_id, current_role, new_review)
    return successBool