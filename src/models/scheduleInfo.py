class ScheduleInfo:
  def __init__(self, title: str, startDate: int, endDate: int, ID: str) -> None:
    self.ID = ID
    self.title = title
    self.startDate = startDate
    self.endDate = endDate