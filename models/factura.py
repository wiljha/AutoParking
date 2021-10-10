from app import database
from datetime import date, time, datetime


class Factura(database.Model):
    __tablename__ = 'facturas'
    
    id_f = database.Column(database.Integer, primary_key=True)
    tiempo = database.Column(database.Integer, nullable=False)
    precio = database.Column(database.Integer, nullable=False)
    id_v = database.Column(database.Integer, database.ForeignKey('vehiculos.id_v'))
    fechaentrada = database.Column(database.String, nullable=False)
    fechasalida = database.Column(database.String, nullable=False)

    id_us = database.Column(database.Integer, database.ForeignKey('usuarios.id'))

    def __init__(self, tiempo, precio, id_v, fechaentrada, fechasalida, id_us):
        self.tiempo = tiempo
        self.precio = precio
        self.id_v = id_v
        self.fechaentrada = fechaentrada
        self.fechasalida = fechasalida
        self.id_us = id_us


    
    def create(self):
        database.session.add(self)
        database.session.commit()

    def __str__(self):
        return f"Factura: {self.id_f} {self.tiempo} {self.precio} {self.id_v} {self.fechaentrada} {self.fechasalida} {self.id_us}"
    
    @staticmethod
    def get_all():
        return Factura.query.all()

    @staticmethod
    def time():    
        factura = Factura.get_all()
        
        time_t = []
        dt = datetime.now()
        fla = 0
        for ti in factura:
            fla = dt.hour -ti.fechaentrada.hour
            time_t.append(fla)
            
                      
            
        return time_t