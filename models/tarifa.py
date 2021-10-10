from app import database
from app import TipoVehiculo

class Tarifa(database.Model):
    __tablename__ = 'tarifas'
    
    id_t = database.Column(database.Integer, primary_key=True)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    valor = database.Column(database.Integer, nullable=False)
    
    def create(self):
        database.session.add(self)
        database.session.commit()
        
    def __init__(self,id_tv,valor):
        self.id_tv = id_tv
        self.valor = valor
        
    def __str__(self):
        return f"<Tarifa: {self.id_t} {self.id_tv} {self.valor}>"
    
    @staticmethod
    def get_all():
        return Tarifa.query.all()
    
    @staticmethod
    def get_full():
        return database.session.query(Tarifa, TipoVehiculo).join(TipoVehiculo).all()
    
    @staticmethod
    def trae_tarifa(id):
        return Tarifa.query.filter_by(id_tv=id).first()
        
    @staticmethod
    def actualiza_tarifa(id,tarifa):
        pre_tarifa = Tarifa.trae_tarifa(id)
        pre_tarifa.valor = tarifa.valor
        database.session.commit()
        
    
