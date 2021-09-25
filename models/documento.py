from sqlalchemy.orm import backref
from app import database

class Documento(database.Model):
    __tablename__ = 'documentos'
    
    id_d = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    usuarios = database.relationship('Usuario', backref='documentos', lazy=True)
    
    def __str__(self):
        return f"<Documento: {self.id_d} {self.nombre}>"
    
    @staticmethod
    def get_all():
        return Documento.query.all()