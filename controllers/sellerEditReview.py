from entity.review import Review

class sellerEditReviewCtl:
  def __init__(self) -> None:
    pass

  def editReview(self, new_review, old_review, agent_id, user_id):
    return Review.editReview(new_review, old_review, agent_id, user_id)