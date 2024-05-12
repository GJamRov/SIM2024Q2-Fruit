from entity.rating import Rating

class buyerEditRatingCtl:
  def __init__(self) -> None:
    pass

  def editRating(self, new_rating, user_id, agent_id):
    successBool = Rating.editRating(new_rating=new_rating, user_id=user_id, agent_id=agent_id)
    return successBool