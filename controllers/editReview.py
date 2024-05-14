from entity.review import Review

class editReviewController:
  def __init__(self) -> None:
    pass

  def editReview(self, review_id, new_review, user_id, role):
    noError = Review.editReview(self, int(review_id), new_review, user_id, role)

    return noError