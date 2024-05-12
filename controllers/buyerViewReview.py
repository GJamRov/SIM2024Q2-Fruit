from entity.review import Review

class buyerViewReviewCtl:

  def __init__(self) -> None:
    pass

  def viewReview(self, agent_id):
  
    review_list = Review.viewReview(agent_id=agent_id)
    return review_list