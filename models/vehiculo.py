from sqlalchemy.orm import backref
from app import database

class Vehiculo(database.Model):
    __tablename__ = 'vehiculos'
    
    id_v = database.Column(database.Integer, primary_key=True)
    placa = database.Column(database.String, nullable=False)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    v_factura = database.relationship('Factura', backref='vehiculos', lazy=True)
    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"<Vehiculo: {self.id_v} {self.placa} {self.id_tv}>"
    
    @staticmethod
    def get_all():
        return Vehiculo.query.all()