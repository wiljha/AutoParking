from sqlalchemy.orm import backref
from app import database
from app import bcrypt

class Usuario(database.Model):
    __tablename__ = 'usuarios'
    
    id_us = database.Column(database.Integer, primary_key=True)
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
    
    def __init__(self, id_d, documento, nombre, apellido, telefono, correo, usuario, password):
        self.id_d = id_d
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.usuario = usuario
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.id_r = 2
        
    def create(self):
        database.session.add(self)
        database.session.commit()
    
    def __str__(self):
        return f"Usuario: {self.id_us} {self.id_d} {self.documento} {self.nombre} {self.apellido} {self.telefono} {self.correo} {self.usuario} {self.password} {self.id_r}"
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def login(username, password):
        validate = False
        
        user = Usuario.query.filter_by(usuario = username).first()
        print(user)
        if user:
            validate = bcrypt.check_password_hash(user.password, password)
        
        return validate