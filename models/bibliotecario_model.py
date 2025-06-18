from database import db

class Bibliotecario(db.Model):
    __tablename__ = "bibliotecario"

    id_biblio = db.Column(db.Integer, primary_key=True)
    turno = db.Column(db.String(50), nullable=False)
    fecha_contratacion = db.Column(db.String(50), nullable=False)

    def __init__(self, turno, fecha_contratacion):
        self.turno = turno
        self.fecha_contratacion = fecha_contratacion

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver categorias
    @staticmethod
    def get_all():
        return Bibliotecario.query.all()
    
    #ver solo una categoria
    @staticmethod
    def get_by_id(id_biblio):
        return Bibliotecario.query.get(id_biblio)
    
    #actualizar
    def update(self, turno=None, fecha_contratacion=None):
        if turno and fecha_contratacion:
            self.turno = turno
            self.fecha_contratacion = fecha_contratacion
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

