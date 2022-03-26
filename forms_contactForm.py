from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length, Email


class SendMessageForm(FlaskForm):
    nombre = StringField(
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ],
        render_kw={"placeholder": "Nombre..."},
    )
    apellido = StringField(
        validators=[
            InputRequired(),
            Length(min=2, max=20),
        ],
        render_kw={"placeholder": "Apellido..."},
    )
    email = EmailField(
        validators=[
            InputRequired("Por favor ingresa tu correo electrónico."),
            Length(min=5, max=60),
        ],
        render_kw={"placeholder": "correo electrónico..."},
    )
    mensaje = TextAreaField(
        validators=[
            InputRequired("Tu mensaje no puede estar vacío..."),
            Length(min=2, max=600),
        ],
        render_kw={"placeholder": "Escribe tu mensaje aquí..."},
    )
    
    submit = SubmitField("ENVIAR")
