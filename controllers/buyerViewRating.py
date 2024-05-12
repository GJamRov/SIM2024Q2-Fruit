from entity.rating import Rating

class buyerViewRatingCtl:
  def __init__(self) -> None:
    pass

  def viewRating(self, agent_id):
    rating = Rating.viewRating(agent_id=agent_id)
    return rating