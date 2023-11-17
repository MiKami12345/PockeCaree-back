from database.db import _connectDB

from models.scheduleInfo import CreateScheduleRequestParam

def insert_schedule(newSchedule: CreateScheduleRequestParam, scheduleID: str):
  try:
    cursor, cnx = _connectDB()

    sql = ('''
      INSERT INTO Schedule 
      (ID, companyID, userID, title, endDate, startDate)
      VALUES (%s, %s, %s, %s, %s, %s)
    ''')

    cursor.execute(sql, (
      scheduleID,
      newSchedule.companyID,
      "1",
      newSchedule.title,
      newSchedule.endDate,
      newSchedule.startDate,
    ))
    cnx.commit()


  except Exception as e:
    print(f"Error in insert_schedule(): {e}")
  finally:
    cursor.close()
    if cnx is not None and cnx.is_connected:
      cnx.close()
  
  return

def get_schedules_by_companyID(companyID: str):
  try:
    cursor, cnx = _connectDB()

    sql = ('''
      SELECT * FROM Schedule
      WHERE companyID = %s
    ''')

    cursor.execute(sql, (companyID, ))
    cnx.commit()

    return cursor.fetchall()


  except Exception as e:
    print(f"Error in get_schedules_by_companyID(): {e}")
  finally:
    cursor.close()
    if cnx is not None and cnx.is_connected:
      cnx.close()
  
  return 