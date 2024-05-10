from entity.rea import REA

class sellerViewReviewCtl:

  def __init__(self) -> None:
    pass

  def view_review(self, agent_id):
  
    review_list = REA.viewReview(agent_id)
    return review_list