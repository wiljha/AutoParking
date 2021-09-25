from sqlalchemy.orm import backref
from app import database

class TipoVehiculo(database.Model):
    __tablename__ = 'tipo_vehiculo'
    
    id_tv = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    tv_tarifa = database.relationship('Tarifa', backref='tipo_vehiculo', lazy=True)
    tv_parqueadero = database.relationship('Parqueadero', backref='tipo_vehiculo', lazy=True)
    tv_vehiculo = database.relationship('Vehiculo', backref='tipo_vehiculo', lazy=True)
    
    def __str__(self):
        return f"<Tipo Vehiculo: {self.id_tv} {self.nombre}>"
    
    @staticmethod
    def get_all():
        return TipoVehiculo.query.all()