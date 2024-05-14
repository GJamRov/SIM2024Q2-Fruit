from entity.review import Review

class giveReviewController:
  def __init__(self) -> None:
    pass

  def giveReview(self, new_review, agent_id, user_id, role):
    noError = Review.giveReview(self, new_review, agent_id, user_id, role)

    return noError