import shortuuid

from models.scheduleInfo import CreateScheduleRequestParam

from database.scheduleTable import insert_schedule

def addNewScheduleLogic(newSchedule: CreateScheduleRequestParam) -> None:
  scheduleID = shortuuid.uuid()

  insert_schedule(newSchedule, scheduleID)

  return 