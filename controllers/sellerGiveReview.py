from entity.rea import REA

class sellerGiveReviewCtl:
  def __init__(self) -> None:
    pass

  def giveReview(self, og_review, new_review, agent_id, user_id):
    noError = REA.giveReview(og_review, new_review, agent_id, user_id)

    return noError