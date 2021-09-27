from sqlalchemy.orm import backref
from app import database

class Rol(database.Model):
    __tablename__ = 'roles'
    
    id_r = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    descripcion = database.Column(database.String, nullable=False)
    usuarios = database.relationship('Usuario', backref='roles', lazy=True)
    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"<Rol: {self.id_r} {self.nombre} {self.descripcion}>"
    
    @staticmethod
    def get_all():
        return Rol.query.all()