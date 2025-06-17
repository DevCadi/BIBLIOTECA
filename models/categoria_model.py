from database import db

class Categoria(db.Model):
    __tablename__ = "categoria"

    id_cat = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver categorias
    @staticmethod
    def get_all():
        return Categoria.query.all()
    
    #ver solo una categoria
    @staticmethod
    def get_by_id(id_cat):
        return Categoria.query.get(id_cat)
    
    #actualizar
    def update(self, nombre=None):
        if nombre:
            self.nombre = nombre
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

