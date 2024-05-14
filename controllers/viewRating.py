from entity.rating import Rating

class viewRatingController:
  def __init__(self) -> None:
    pass

  def viewRating(self, agent_id, role):
    rating = Rating.viewRating(self, agent_id, role)
    return rating

