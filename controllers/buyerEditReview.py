from entity.rea import REA

class buyerEditReviewCtl:
  def __init__(self) -> None:
    pass

  def editReview(self, new_review, old_review, agent_id, user_id):
    return REA.editReview(new_review=new_review, old_review=old_review, agent_id=agent_id, user_id=user_id)