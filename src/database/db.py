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

    # Companyテーブルの初期化
    try:
        # Companyテーブルがあるかの問い合わせ
        sql = '''
            SELECT * FROM Company LIMIT 1;
        '''
        cursor.execute(sql)
        print("Companyテーブルがありました。")
    except Exception as e:
        print("Companyテーブルがありませんでした。")

        # Companyテーブルの作成
        sql = '''
            CREATE TABLE Company (
                companyID VARCHAR(255),
                companyName VARCHAR(255) NOT NULL,
                memo VARCHAR(255),
                status int NOT NULL,
                mypageURL VARCHAR(255),
                PRIMARY KEY (CompanyID)
            );
        '''
        cursor.execute(sql)
        print("Companyテーブルを作成しました。")


    # Scheduleテーブルの初期化
    try:
        # Scheduleテーブルがあるかの問い合わせ
        sql = '''
            SELECT * FROM Schedule LIMIT 1;
        '''
        cursor.execute(sql)
        print("Scheduleテーブルがありました。")
    except Exception as e:
        print("Scheduleテーブルがありませんでした。")

        # Scheduleテーブルの作成
        sql = '''
            CREATE TABLE Schedule (
                ID VARCHAR(255) PRIMARY KEY,
                companyID VARCHAR(255) NOT NULL,
                userID VARCHAR(255) NOT NULL,
                title VARCHAR(255) NOT NULL,
                endDate INT,
                startDate INT
            );
        '''
        cursor.execute(sql)
        print("Scheduleテーブルを作成しました。")
  except Exception as e:
    print(f"Error: {e}")
  finally:
    if cnx is not None and cnx.is_connected:
      cnx.close()
  


  