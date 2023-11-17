class CreateScheduleRequestParam:
  def __init__(self, companyID: str, title: str, endDate: int, startDate: int) -> None:
    self.companyID = companyID
    self.title = title
    self.endDate = endDate
    self.startDate = startDate

class ScheduleInfo:
  def __init__(self, title: str, startDate: int, endDate: int) -> None:
    self.title = title
    self.startDate = startDate
    self.endDate = endDate
