from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

#'postgresql://username:password@host:port/database'

uri = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1' # produccion

from config import config
uri = config() # megavas

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from models.rol import Rol
from models.documento import Documento
from models.tarifa import Tarifa
from models.usuario import Usuario
from models.parqueadero import Parqueadero
from models.tipovehiculo import TipoVehiculo
from models.vehiculo import Vehiculo
from models.factura import Factura
#from models.prueba import Prueba

@app.route("/")
def hello():
    doc_user = ''
    usuarios = Usuario.get_all()
    for user in usuarios:
        doc_user += user.documento + ' '
        print(user)
    
    return doc_user


@app.route("/register")
def register():
    t_doc = 1
    documento = 987654
    usuario = 'usuario1'
    password = '123456'
    
    user = Usuario(t_doc, documento, usuario, password)
    
    return str(bcrypt.check_password_hash(user.password, password))
    
