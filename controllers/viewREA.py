from entity.rating import Rating

class viewREA:
  def __init__(self) -> None:
    pass

  def viewREATable(self):
    rea_table = Rating.returnRatingTable(self)
    return rea_table