import shortuuid

from models.companyInfo import CreateCompanyRequestParam

from database.companyTable import insert_company

def addNewCompanyLogic(newCompany: CreateCompanyRequestParam) -> None:
  companyID = shortuuid.uuid()

  insert_company(newCompany, companyID)

  return 