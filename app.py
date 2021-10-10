import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import current_user, login_user, login_required, LoginManager, logout_user
from flask_session import Session
from config_lang import ConfigLang
from datetime import date, time, datetime

login_manager = LoginManager()


app = Flask(__name__)


#'postgresql://username:password@host:port/database'

uri = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1' # produccion

#from config import config
#uri = config() # megavas

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(32)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager.init_app(app)
login_manager.login_view = "index"

from models.rol import Rol
from models.documento import Documento
from models.tipovehiculo import TipoVehiculo
from models.tarifa import Tarifa
from models.usuario import Usuario
from models.parqueadero import Parqueadero
from models.vehiculo import Vehiculo
from models.factura import Factura



langIni = 'lang_ESP.ini'

@app.route("/", methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        usuario = request.form["user"]
        password = request.form["pass"]
        
        validate = Usuario.login(usuario, password)
        print(validate[1])
        if validate[0]:
            login_user(validate[1])
            return redirect(url_for("users"))
    
    lang = ConfigLang(langIni, 'LOGIN')
    return render_template('index.html', lang=lang)

@app.route("/ventas", methods=["GET", "POST"])
def ventas():
    lang = ConfigLang(langIni, 'LOGIN')
    factura = Factura.get_all()
    time = Factura.time()
    results = database.session.query(Factura, Vehiculo, TipoVehiculo). \
            select_from(Factura).join(Vehiculo).join(TipoVehiculo).all()
    #print(results)
    if request.method == 'POST':
        plac = request.form['placa']
        tvehic= request.form['Tvehiculo']
        fechaentrada = datetime.now()
        vehiculo = Vehiculo.if_exist(plac)
        
        
        if vehiculo:
            pass
        else:
            tempVehiculo = Vehiculo(plac,tvehic)
            tempVehiculo.create()
            vehiculo = tempVehiculo.get_id(plac)
            
        
        

        idvec = vehiculo.id_v
        fac = Factura(0,0,idvec,fechaentrada,'00:00:00',2)
        fac.create()
        #print(plac)
        return render_template('ventas.html',  results=results, tiempo=time)
    else:
        factura = Factura.get_all()
        time = Factura.time()
        
    

    if request.method == 'GET':
        reqfac = request.args.get('out_id')
        fil = database.session.query(Vehiculo.placa,TipoVehiculo.nombre, Factura.fechaentrada).join(Factura).join(TipoVehiculo). \
            filter(Factura.id_f==reqfac).all()
        print(fil)
        print(type(fil))
        dt = datetime.now()
        ff =[]
        for tes in fil:
            ff+=tes
    
        dt = datetime.now().time()
        
        return render_template('ventas.html',  results=results, tiempo=time, ff=ff, dt=dt)
    else:
        pass   

        Tvehiculo = TipoVehiculo.get_all()

        time_now =Factura.time()
        
        
        dt = datetime.now()
       

        return render_template('ventas.html',  results=results, tiempo=time,dt=dt,lang=lang)


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

    


    
    
       
    
