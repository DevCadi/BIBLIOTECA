from database import db

class Audio(db.Model):
    __tablename__ = "audio"

    id_audio = db.Column(db.Integer, primary_key=True)
    duracion = db.Column(db.Float, nullable=False)
    formato = db.Column(db.String(50), nullable=False)
    propietario = db.Column(db.String(150), nullable=False)

    def __init__(self, duracion, formato, propietario):
        self.duracion = duracion
        self.formato = formato
        self.propietario = propietario

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver categorias
    @staticmethod
    def get_all():
        return Audio.query.all()
    
    #ver solo una categoria
    @staticmethod
    def get_by_id(id_audio):
        return Audio.query.get(id_audio)
    
    #actualizar
    def update(self, duracion=None, formato=None, propietario=None):
        if duracion and formato and propietario:
            self.duracion = duracion
            self.formato = formato
            self.propietario = propietario
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

