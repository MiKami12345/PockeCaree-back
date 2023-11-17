from models.companyInfo import ChangeCompanyStatusRequestParam

from database.companyTable import update_company_status

def updateCompanyStatusLogic(newStatus: ChangeCompanyStatusRequestParam) -> None:
  update_company_status(newStatus)

  return