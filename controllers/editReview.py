from entity.review import Review

class editReviewController:
  def __init__(self) -> None:
    pass

  def editReview(self, new_review, agent_id, user_id, role):
    noError = Review.editReview(self, new_review, agent_id, user_id, role)

    return noError