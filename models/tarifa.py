from app import database

class Tarifa(database.Model):
    __tablename__ = 'tarifas'
    
    id_t = database.Column(database.Integer, primary_key=True)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    valor = database.Column(database.Integer, nullable=False)
    
    def __str__(self):
        return f"<Tarifa: {self.id_t} {self.id_tv} {self.valor}>"
    
    @staticmethod
    def get_all():
        return Tarifa.query.all()