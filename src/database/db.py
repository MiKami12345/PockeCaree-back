import mysql.connector

from setting import *

# DBに接続する
def _connectDB(isDict = True):
  cnx = mysql.connector.connect(
    database=MYSQL_DATABASE,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
  )

  cursor = cnx.cursor(buffered=True, dictionary=isDict)

  return cursor, cnx

def init_db():
  try:
    cursor, cnx = _connectDB()
  except Exception as e:
    print(f"Error: {e}")
  finally:
    if cnx is not None and cnx.is_connected:
      cnx.close()