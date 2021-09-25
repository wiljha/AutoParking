from app import database

#importa los modelos
from models.documento import Documento
from models.tarifa import Tarifa
from models.usuario import Usuario
from models.parqueadero import Parqueadero
from models.tipovehiculo import TipoVehiculo
from models.vehiculo import Vehiculo
from models.factura import Factura

#refresca la dd
database.create_all()