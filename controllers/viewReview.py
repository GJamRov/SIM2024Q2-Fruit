from entity.review import Review

class viewReviewController:
  def __init__(self) -> None:
    pass

  def viewReview(self, user_id, role):
  
    review_list = Review.viewReview(self, user_id, role)

    return review_list
    