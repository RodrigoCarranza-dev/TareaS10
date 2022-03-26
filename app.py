from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes_messages import messages
from routes_main import main
from utils_db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(main)
app.register_blueprint(messages)