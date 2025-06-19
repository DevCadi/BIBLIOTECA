from database import db

class Proyecto(db.Model):
    __tablename__ = "proyecto_academico"

    id_pro = db.Column(db.Integer, primary_key=True)
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), nullable=False)
    autor_est = db.Column(db.String(50), nullable=False)
    anio_defensa = db.Column(db.Integer, nullable=False)

    material = db.relationship('Material', back_populates = 'proyecto_academico')

    def __init__(self, id_material ,autor_est, anio_defensa):
        self.id_material = id_material
        self.autor_est = autor_est
        self.anio_defensa = anio_defensa

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver 
    @staticmethod
    def get_all():
        return Proyecto.query.all()
    
    #ver solo uno
    @staticmethod
    def get_by_id(id_pro):
        return Proyecto.query.get(id_pro)
    
    #actualizar
    def update(self, id_material=None ,autor_est=None, anio_defensa=None):
        if autor_est and id_material and anio_defensa:
            self.id_material = id_material
            self.autor_est = autor_est
            self.anio_defensa = anio_defensa
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

