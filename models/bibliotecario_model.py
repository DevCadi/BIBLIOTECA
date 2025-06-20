from database import db
from models.usuario_model import Usuario  # Asegúrate que la ruta sea correcta

class Bibliotecario(db.Model):
    __tablename__ = "bibliotecario"

    id_biblio = db.Column(db.Integer, primary_key=True)
    turno = db.Column(db.String(50), nullable=False)
    fecha_contratacion = db.Column(db.String(50), nullable=False)

    # Relación con Usuario
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship('Usuario', backref=db.backref('bibliotecario', uselist=False))

    def __init__(self, turno, fecha_contratacion, id_usuario):
        self.turno = turno
        self.fecha_contratacion = fecha_contratacion
        self.id_usuario = id_usuario

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Bibliotecario.query.all()

    @staticmethod
    def get_by_id(id_biblio):
        return Bibliotecario.query.get(id_biblio)

    def update(self, turno=None, fecha_contratacion=None):
        if turno:
            self.turno = turno
        if fecha_contratacion:
            self.fecha_contratacion = fecha_contratacion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
