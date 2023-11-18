import shortuuid

from models.companyInfo import CompanySummaryResponseParam, CompanyInfoResponseParam
from models.scheduleInfo import ScheduleInfo

from database.companyTable import get_company_by_userID, get_company_by_companyID
from database.scheduleTable import get_schedules_by_companyID

def getCompanyLogicByUserID(userID: str) -> list[CompanySummaryResponseParam]:
  companyData = get_company_by_userID(userID)

  scheduleDataList = {}
  for company in companyData:
    scheduleData = get_schedules_by_companyID(company["companyID"].decode())
    if len(scheduleData) != 0:
      scheduleDataList[company["companyID"].decode()] = scheduleData[0]

  companyInfoList: list[CompanySummaryResponseParam] = []
  for company in companyData:
    if company["companyID"].decode() in scheduleDataList:
      nextSchedules=ScheduleInfo(
        title=scheduleDataList[company["companyID"].decode()]["title"].decode(),
        startDate=scheduleDataList[company["companyID"].decode()]["startDate"],
        endDate=scheduleDataList[company["companyID"].decode()]["endDate"],
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
    print(company)
    print(nextSchedules)

  companyInfoListDict = []
  for cil in companyInfoList:
    companyInfoListDict.append(cil.__dict__)
  
  return companyInfoListDict


def getCompanyLogicByCompanyID(companyID: str):
  companyData = get_company_by_companyID(companyID)
  scheduleData = get_schedules_by_companyID(companyID)

  schedules = []
  for schdeule in scheduleData:
    schedules.append(
      ScheduleInfo(
        title=schdeule["title"].decode(),
        startDate=schdeule["startDate"],
        endDate=schdeule["endDate"],
      ).__dict__
    )
  
  print(companyData)
  company = CompanyInfoResponseParam(
    companyName=companyData["companyName"].decode(),
    mypageURL=companyData["mypageURL"].decode(),
    memo=companyData["memo"].decode(),
    status=companyData["memo"].decode(),
    schedules=schedules,
  )

  return company.__dict__