from app import database

class Parqueadero(database.Model):
    __tablename__ = 'parqueaderos'
    
    id_p = database.Column(database.Integer, primary_key=True)
    capacidad = database.Column(database.Integer, nullable=False)
    id_tv = database.Column(database.Integer, database.ForeignKey('tipo_vehiculo.id_tv'))
    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"<Parqueadero: {self.id_p} {self.capacidad} {self.id_tv}>"
    
    @staticmethod
    def get_all():
        return Parqueadero.query.all()