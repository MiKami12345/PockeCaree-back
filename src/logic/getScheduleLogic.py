import shortuuid
from models.scheduleInfo import CreateScheduleRequestParam, ScheduleInfo

from database.scheduleTable import get_schedules_by_companyID

def getScheduleLogic(companyID: str) -> list[CreateScheduleRequestParam]:
  scheduleInfoData = get_schedules_by_companyID(companyID)

  scheduleInfoList = []
  for schedule in scheduleInfoData:
    scheduleInfoList.append(
      ScheduleInfo(
        title=schedule["title"].decode(),
        startDate=schedule["startDate"],
        endDate=schedule["endDate"],
      ).__dict__
    )

  return scheduleInfoList