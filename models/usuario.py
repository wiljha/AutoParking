from sqlalchemy.orm import backref
from app import database

class Usuario(database.Model):
    __tablename__ = 'usuarios'
    
    id_us = database.Column(database.Integer, primary_key=True)
    id_d = database.Column(database.Integer, database.ForeignKey('documentos.id_d'))
    documento = database.Column(database.String, nullable=False)
    nombre = database.Column(database.String, nullable=True)
    apellido = database.Column(database.String, nullable=True)
    telefono = database.Column(database.String, nullable=True)
    correo = database.Column(database.String, nullable=True)
    usuario = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)
    u_factura = database.relationship('Factura', backref='usuarios', lazy=True)
    
    def __str__(self):
        return f"Usuario: {self.id_us} {self.id_d} {self.documento} {self.nombre} {self.apellido} {self.telefono} {self.correo} {self.usuario} {self.password}"
    
    @staticmethod
    def get_all():
        return Usuario.query.all()