from utils_db import db 

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    mensaje = db.Column(db.String(600), nullable=False)

    def __init__(self, nombre, apellido, email, mensaje) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.mensaje = mensaje


    def __repr__(self) -> str:
        return f"Message({self.id}, {self.nombre}, '{self.apellido}', '{self.email}' , '{self.mensaje}')"
    