from flask import Blueprint, render_template, redirect, url_for
from utils_db import db
from models_message import Message

messages = Blueprint("messages", __name__, url_prefix="/messages")

@messages.route("/")
def home():
    bandejaEntrada = Message.query.all()
    return render_template("messages.html", mensajes = bandejaEntrada)