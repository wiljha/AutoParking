from app import database

class Prueba(database.Model):
    __tablename__ = 'pruebas'
    
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    apellido = database.Column(database.String, nullable=False)
    fecha = database.Column(database.String, nullable=True)

    @staticmethod
    def get_all():
        return Prueba.query.all()