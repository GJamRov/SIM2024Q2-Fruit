from entity.rating import Rating

class sellerGiveRatingCtl:
  def __init__(self) -> None:
    pass

  def giveRating(self, new_rating, user_id, agent_id):
    successBool = Rating.giveRating(new_rating=new_rating, user_id=user_id, agent_id=agent_id)
    return successBool