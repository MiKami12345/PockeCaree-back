import shortuuid

from models.companyInfo import CompanySummaryResponseParam
from models.scheduleInfo import ScheduleInfo

from database.companyTable import get_company_by_userID
from database.scheduleTable import get_schedules_by_companyID

def getCompanyLogicByUserID(userID: str) -> list[CompanySummaryResponseParam]:
  companyData = get_company_by_userID(userID)

  companyIDList: list[str] = []
  for company in companyData:
    companyIDList.append(company["companyID"])

  nextSchedules = get_schedules_by_companyID(companyIDList)
  
  scheduleDict = {}
  for schedule in nextSchedules:
    scheduleDict[schedule["companyID"].decode()] = schedule

  companyInfoList: list[CompanySummaryResponseParam] = []
  for company in companyData:
    if company["companyID"].decode() in scheduleDict:
      nextSchedules=ScheduleInfo(
        title=scheduleDict[company["companyID"].decode()]["title"].decode(),
        startDate=scheduleDict[company["companyID"].decode()]["startDate"],
        endDate=scheduleDict[company["companyID"].decode()]["endDate"],
      ).__dict__
    else:
      nextSchedules={}

    companyInfoList.append(
      CompanySummaryResponseParam(
        companyName=company["companyName"].decode(),
        memo=company["memo"].decode(),
        status=company["status"],
        nextSchedule=nextSchedules
      )
    )

  companyInfoListDict = []
  for cil in companyInfoList:
    companyInfoListDict.append(cil.__dict__)
  
  return companyInfoListDict
