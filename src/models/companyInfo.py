from models.scheduleInfo import ScheduleInfo

class CreateCompanyRequestParam:
  def __init__(self, companyName: str, mypageURL: str, memo: str, status: int) -> None:
    self.companyName = companyName
    self.mypageURL = mypageURL
    self.memo = memo
    self.status = status

# 一覧ページ
class CompanySummaryResponseParam:
  def __init__(self, companyName: str, memo: str, status: int, nextSchedule: ScheduleInfo) -> None:
    self.companyName = companyName
    self.memo = memo
    self.status = status
    self.nextSchedule = nextSchedule

# 詳細ページ
class CompanyInfoResponseParam:
  def __init__(self, companyName: str, mypageURL: str, memo: str, status: int) -> None:
    self.companyName = companyName
    self.mypageURL = mypageURL
    self.memo = memo
    self.status = status