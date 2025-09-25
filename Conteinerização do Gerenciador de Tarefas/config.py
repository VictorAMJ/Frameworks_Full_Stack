from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SWAGGER = {
    "title": "Gerenciador de Tarefas",
    "uiversion": 3 
}


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)