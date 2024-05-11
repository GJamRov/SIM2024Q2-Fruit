from entity.rea import REA

class sellerEditRatingCtl:
  def __init__(self) -> None:
    pass

  def editRating(self, new_rating, user_id, agent_id):
    successBool = REA.editRating(new_rating=new_rating, user_id=user_id, agent_id=agent_id)

    return successBool