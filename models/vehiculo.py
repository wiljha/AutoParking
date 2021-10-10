from sqlalchemy.orm import backref
from app import database

class Vehiculo(database.Model):
    __tablename__ = 'vehiculos'
    
    id_v = database.Column(database.Integer, primary_key=True)
    placa = database.Column(database.String, nullable=False)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    v_factura = database.relationship('Factura', backref='vehiculos', lazy=True)

    def __init__(self, placa, id_tv):
        self.placa = placa
        self.id_tv = id_tv 
    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"<Vehiculo: {self.id_v} {self.placa} {self.id_tv}>"
    
    @staticmethod
    def get_all():
        return Vehiculo.query.all()

    @staticmethod
    def get_id(placa):
        
        return Vehiculo.query.filter_by(placa = placa).first()    

    @staticmethod
    def if_exist(placa):
        validate = 0
        vehiculo = Vehiculo.get_id(placa)
        return vehiculo