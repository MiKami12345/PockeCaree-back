from flask import Flask, request, jsonify
from flask_cors import CORS

import database.db as db
from models.companyInfo import CreateCompanyRequestParam

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

  

  return 404

# 企業のステータスを変更する
@app.route("/company/status", methods=['POST'])
def update_company_status_controller():
  return 404

# 企業情報取得する
@app.route("/company", methods=['GET'])
def get_company_controller():
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