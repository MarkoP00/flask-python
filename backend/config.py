from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=['http://localhost:5173', "https://expensetracker-fullstack.netlify.app"], supports_credentials=True,
     methods=["GET", "POST", "PATCH", "DELETE"], allow_headers=["Content-Type", "Authorization"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
