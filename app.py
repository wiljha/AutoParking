from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#params = config()

#'postgresql://username:password@host:port/database'

uri = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1' # produccion

"""from config import config
uri = config() # megavas"""

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
from models.documento import Documento
from models.usuario import Usuario
#from models.prueba import Prueba

@app.route("/")
def hello():
    doc_user = ''
    usuarios = Usuario.get_all()
    for user in usuarios:
        doc_user += user.documento + ' '
        print(user)
    
    return doc_user
