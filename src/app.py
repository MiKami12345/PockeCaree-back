from flask import Flask, request, jsonify
from flask_cors import CORS

import database.db as db
from models.companyInfo import CreateCompanyRequestParam, ChangeCompanyStatusRequestParam
from models.scheduleInfo import CreateScheduleRequestParam

from logic.addNewCompanyLogic import addNewCompanyLogic
from logic.getCompanyLogic import getCompanyLogicByUserID
from logic.updateCompanyStatusLogic import updateCompanyStatusLogic

from logic.addNewScheduleLogic import addNewScheduleLogic
from logic.getScheduleLogic import getScheduleLogic

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
# 企業情報のサマリーを返す
# 企業IDを受け取って、その企業の詳細情報を返す
@app.route("/company", methods=['GET'])
def get_company_controller():
  # req = request.args
  # user_id = req.get("userID")
  userID = '1'
  companys = getCompanyLogicByUserID(userID)

  return jsonify(companys), 200



  


# 予定に関するAPI
# 新しい予定を追加
@app.route("/schedule", methods=['POST'])
def add_schedule_controller():
  newSchedule = CreateScheduleRequestParam(**request.json)
  
  addNewScheduleLogic(newSchedule)
  return jsonify({}), 200

# 予定を取得して返す
@app.route("/schedule", methods=['GET'])
def get_schedule_controller():
  req = request.args
  companyID = req.get("companyID")
  print(companyID)

  schedules = getScheduleLogic(companyID)

  return jsonify(schedules), 200
  
if __name__ == '__main__':
  db.init_db()
  app.run(debug=False, host='0.0.0.0', port=5000)