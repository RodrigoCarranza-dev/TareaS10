from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.messages import messages
from routes.main import main
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(main)
app.register_blueprint(messages)