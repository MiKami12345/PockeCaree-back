from database.db import _connectDB

from models.companyInfo import CreateCompanyRequestParam, ChangeCompanyStatusRequestParam

def insert_company(newCompany: CreateCompanyRequestParam, companyID: str):
  try:
    cursor, cnx = _connectDB()

    sql = ('''
      INSERT INTO Company 
      (companyID, companyName, memo, status, mypageURL, userID)
      VALUES (%s, %s, %s, %s, %s, %s)
    ''')

    cursor.execute(sql, (
      companyID,
      newCompany.companyName,
      newCompany.memo,
      newCompany.status,
      newCompany.mypageURL,
      "1",
    ))
    cnx.commit()
  except Exception as e:
    print(f"Error in insert_company(): {e}")
  finally:
    cursor.close()
    if cnx is not None and cnx.is_connected:
      cnx.close()
  
  return

def update_company_status(newStatus: ChangeCompanyStatusRequestParam):
  print(newStatus.companyID)
  try:
    cursor, cnx = _connectDB()

    sql = ('''
      UPDATE Company
      SET status=%s
      WHERE companyID=%s
    ''')

    cursor.execute(sql, (
      newStatus.newStatus,
      newStatus.companyID,
    ))
    cnx.commit()

  except Exception as e:
    print(f"Error in update_company_status(): {e}")
  finally:
    cursor.close()
    if cnx is not None and cnx.is_connected:
      cnx.close()
  
  return

def get_company_by_userID(userID: str):
  cursor, cnx = _connectDB()

  sql = '''SELECT * FROM Company WHERE userID = %s'''
  cursor.execute(sql, (userID, ))
  companyInfo = cursor.fetchall()

  cursor.close()
  cnx.close()

  return companyInfo

def get_company_by_companyID():

  # TODO
  return