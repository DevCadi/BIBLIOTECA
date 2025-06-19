from database import db

class Video(db.Model):
    __tablename__ = "video"

    id_video = db.Column(db.Integer, primary_key=True)
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), nullable=False)
    duracion = db.Column(db.Float, nullable=False)
    formato = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(150), nullable=False)

    material = db.relationship('Material', back_populates='video')

    def __init__(self, id_material,duracion, formato, director):
        self.id_material = id_material
        self.duracion = duracion
        self.formato = formato
        self.director = director

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver categorias
    @staticmethod
    def get_all():
        return Video.query.all()
    
    #ver solo una categoria
    @staticmethod
    def get_by_id(id_video):
        return Video.query.get(id_video)
    
    #actualizar
    def update(self, id_material=None ,duracion=None, formato=None, director=None):
        if id_material and duracion and formato and director:
            self.id_material = id_material
            self.duracion = duracion
            self.formato = formato
            self.director = director
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

