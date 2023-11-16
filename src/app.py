from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_database_user:your_database_password@localhost/your_database_name'
db = SQLAlchemy(app)
