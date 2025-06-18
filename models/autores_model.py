from database import db

class Autores(db.Model):
    __tablename__ = "autores"

    id_autor = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    apellidos = db.Column(db.String(100),nullable=False)


    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    
    #tener un obj de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #método para devolver los usuarios de la tabla usuarios
    @staticmethod #no depende de la clase
    def get_all():
        return Autores.query.all()
    
    #metodo para recuperar un solo registro
    @staticmethod
    def get_by_id(id):
        return Autores.query.get(id)
    
    #metodo para actualizar
    def update(self, nombre=None, apellidos=None):
        if nombre and apellidos:
            self.nombre = nombre
            self.apellidos = apellidos
        db.session.commit()
    
    #metodo delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()