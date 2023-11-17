from flask import Flask, request, jsonify
from flask_cors import CORS

import database.db as db
from models.companyInfo import CreateCompanyRequestParam

from logic.addNewCompanyLogic import addNewCompanyLogic
from logic.getCompanyLogic import getCompanyLogic

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['GET', 'POST'])
def getTest():
  if request.method == 'POST':
    return jsonify({"data": "post", }), 200
  elif request.method == 'GET':
    return jsonify({"data": "get", }), 200
  else:
    return 404


# 企業情報に関するAPI
# 新しい企業を追加
@app.route("/company", methods=['POST'])
def add_company_controller():
  newCompany = CreateCompanyRequestParam(**request.json)
  
  addNewCompanyLogic(newCompany)
  return jsonify({}), 200

# 企業のステータスを変更する
@app.route("/company/status", methods=['POST'])
def update_company_status_controller():
  newStatusObj = ChangeCompanyStatusRequestParam(**request.json)

  updateCompanyStatusLogic(newStatusObj)

  return jsonify({}), 200

# 企業情報取得する
# localhost:5000/company?id=1
@app.route("/company", methods=['GET'])
def get_company_controller():
  try:
    # req = request.args
    # user_id = req.get("userId")
    userId = 1

    try:
      return jsonify(getCompanyLogic(userId)), 200
    except Exception as e:
      print(e)
      return 404


  # 企業情報のサマリーを返す
  
  # 企業IDを受け取って、その企業の詳細情報を返す
  except Exception as e:
    print(e)
    return 500

  
  return 404


# 予定に関するAPI
# 新しい予定を追加
@app.route("/schedule", methods=['POST'])
def add_schedule_controller():
  return 404

# 予定を取得する
@app.route("/schedule", methods=['GET'])
def get_schedule_controller():
  return 404

if __name__ == '__main__':
  db.init_db()
  app.run(debug=False, host='0.0.0.0', port=5000)