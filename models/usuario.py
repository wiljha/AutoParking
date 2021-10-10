from sqlalchemy.orm import backref
from app import database, bcrypt, login_manager, Rol
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

class Usuario(database.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = database.Column(database.Integer, primary_key=True)
    id_d = database.Column(database.Integer, database.ForeignKey('documentos.id_d'))
    documento = database.Column(database.String, nullable=False)
    nombre = database.Column(database.String, nullable=True)
    apellido = database.Column(database.String, nullable=True)
    telefono = database.Column(database.String, nullable=True)
    correo = database.Column(database.String, nullable=True)
    usuario = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)
    id_r = database.Column(database.Integer, database.ForeignKey('roles.id_r'))
    u_factura = database.relationship('Factura', backref='usuarios', lazy=True)
    
    def __init__(self, id_d, documento, nombre, apellido, telefono, correo, usuario, password, id_r):
        self.id_d = id_d
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.usuario = usuario
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.id_r = id_r
        
    def create(self):
        database.session.add(self)
        database.session.commit()
    
    def __str__(self):
        return f"Usuario: {self.id} {self.id_d} {self.documento} {self.nombre} {self.apellido} {self.telefono} {self.correo} {self.usuario} {self.password} {self.id_r}"
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_full():
        return database.session.query(Usuario, Rol).join(Rol).all()

    @staticmethod
    def login(username, password):
        validate = []
        validate.append(False)
        
        user = Usuario.query.filter_by(usuario = username).first()
        if user:
            validate[0] = bcrypt.check_password_hash(user.password, password)
            validate.append(user)
        
        return validate
    
    @staticmethod
    def if_noexist(doc, tipo):
        validate = True
        
        user = Usuario.query.filter_by(documento = doc).first()
        if user:
            if user.id_r == int(tipo):
                validate = False
        
        return validate
    
    @staticmethod
    def get_user(id):
        #return Usuario.query.filter_by(id = id).first()
        return Usuario.query.get(id)
    
    @staticmethod
    def update_user(id, user):
        pre_usuario = Usuario.get_user(id)
        pre_usuario.id_d = user.id_d
        pre_usuario.documento = user.documento
        pre_usuario.nombre = user.nombre
        pre_usuario.apellido = user.apellido
        pre_usuario.telefono = user.telefono
        pre_usuario.correo = user.correo
        pre_usuario.usuario = user.usuario
        pre_usuario.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
        pre_usuario.id_r = int(user.id_r)
        database.session.commit()