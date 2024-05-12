from entity.rea import REA
class reaViewReviewCtl:
  def __init__(self) -> None:
    pass

  def viewReview(self, agent_id):
    review_list = REA.viewReview(agent_id=agent_id)
    return review_list