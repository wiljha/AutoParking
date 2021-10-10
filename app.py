from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect
from config_lang import ConfigLang



app = Flask(__name__)

#'postgresql://username:password@host:port/database'

uri = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1' # produccion

#refrescafrom config import config
#uri = config() # megavas

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from models.rol import Rol
from models.documento import Documento
from models.tipovehiculo import TipoVehiculo
from models.tarifa import Tarifa
from models.usuario import Usuario
from models.parqueadero import Parqueadero
from models.vehiculo import Vehiculo
from models.factura import Factura

langIni = 'lang_ESP.ini'

@app.route("/")
def hello():
    lang = ConfigLang(langIni, 'LOGIN')
    return render_template('index.html', lang=lang)


@app.route("/register", methods=["GET", "POST"])
def register():
    if(request.method == "POST"):
        t_doc = request.form["rol"]
        documento = request.form["documento"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        telefono = request.form["tel"]
        correo = request.form["emal"]
        usuario = request.form["user"]
        password = request.form["pass"]
        
        user = Usuario(t_doc, documento, nombre, apellido, telefono, correo, usuario, password)
        user.create()
    
    return render_template('usuarios.html')

@app.route("/login")
def login():
    usuario = 'usuario2'
    password = '123456'
    
    return str(Usuario.login(usuario, password))

@app.route("/tarifas", methods=["GET","POST"])
def tarifas():
    tarifa=Tarifa.get_full()
    bici=Tarifa.trae_tarifa(1)  
    moto=Tarifa.trae_tarifa(2) 
    auto=Tarifa.trae_tarifa(3)  
    if request.method == 'POST':
       valor1=request.form["bici"]
       valor2=request.form["moto"]
       valor3=request.form["auto"]
       tar=Tarifa(1,valor1)
       print(tar)
       tar.actualiza_tarifa(1,tar)
       tar=Tarifa(2,valor2)
       tar.actualiza_tarifa(2,tar)
       tar=Tarifa(3,valor3)
       tar.actualiza_tarifa(3,tar)
    return render_template('tarifas.html',tarifa=tarifa,bici=bici.valor,moto=moto.valor,auto=auto.valor)

    


    
    
       
    
