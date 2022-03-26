import email
from flask import Blueprint, render_template, redirect, url_for
from forms.contactForm import SendMessageForm
from utils.db import db
from models.message import Message

main = Blueprint("main", __name__, url_prefix="/")

@main.route("/", methods=["GET", "POST"])
def crearMensaje():
    form = SendMessageForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        mensaje = form.mensaje.data
        nuevoregistro = Message(nombre, apellido, email, mensaje)
        db.session.add(nuevoregistro)
        db.session.commit()
    return render_template("main.html", form=form)