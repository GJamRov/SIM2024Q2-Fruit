from entity.review import Review

class sellerGiveReviewCtl:
  def __init__(self) -> None:
    pass

  def giveReview(self, new_review, agent_id, user_id):
    noError = Review.giveReview(new_review=new_review, agent_id=agent_id, user_id=user_id)

    return noError