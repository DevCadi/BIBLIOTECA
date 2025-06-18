from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    apellido = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    telefono = db.Column(db.String(20),nullable=False)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String,nullable=False)
    tipo = db.Column(db.String(20),nullable=False)

    def __init__(self, nombre, apellido, email, telefono, username, password, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.username = username
        self.password = self.hash_password(password)
        self.tipo = tipo
    
    @staticmethod #no depende
    def hash_password(password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    #tener un obj de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #método para devolver los usuarios de la tabla usuarios
    @staticmethod #no depende de la clase
    def get_all():
        return Usuario.query.all()
    
    #metodo para recuperar un solo registro
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    #metodo para actualizar
    def update(self, nombre=None, apellido=None, email=None, telefono=None, username=None, password=None, tipo=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if username:
            self.username = username
        if password:
            self.password = self.hash_password(password)
        if tipo:
            self.tipo = tipo
        db.session.commit()
    
    #metodo delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "username": self.username,
            "tipo": self.tipo
            # No incluimos la contraseña por seguridad
        }