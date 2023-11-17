from flask import Flask, request, jsonify
import database.db as db

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


if __name__ == '__main__':
  db.init_db()
  app.run(debug=False, host='0.0.0.0', port=5000)