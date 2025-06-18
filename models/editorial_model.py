from database import db

class Editorial(db.Model):
    __tablename__ = "editorial"

    id_edi = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver 
    @staticmethod
    def get_all():
        return Editorial.query.all()
    
    #ver solo uno
    @staticmethod
    def get_by_id(id_edi):
        return Editorial.query.get(id_edi)
    
    #actualizar
    def update(self, nombre=None, pais=None):
        if nombre and pais:
            self.nombre = nombre
            self.pais = pais
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

