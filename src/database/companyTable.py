from database.db import _connectDB

from models.companyInfo import CreateCompanyRequestParam

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

    # for debug
    sql = '''
      SELECT * FROM Company
      WHERE companyID = %s
    '''

    cursor.execute(sql, (companyID, ))
    print(cursor.fetchall()[0])
  except Exception as e:
    print(f"Error in insert_company(): {e}")
  finally:
    cursor.close()
    if cnx is not None and cnx.is_connected:
      cnx.close()
  
  return

def update_company_status():
  # TODO
  print("update company status.")

def get_company_by_userID(userID: int):
  # TODO
  return

def get_company_by_companyID():

  # TODO
  return