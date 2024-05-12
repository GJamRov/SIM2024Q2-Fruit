from entity.rea import REA

class reaViewRatingCtl:
  def __init__(self) -> None:
    pass

  def viewRating(self, agent_id):
    rating = REA.viewRating(agent_id=agent_id)
    return rating