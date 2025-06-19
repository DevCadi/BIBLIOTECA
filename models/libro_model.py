from database import db

class Libro(db.Model):
    __tablename__ = 'libros'

    id_libro = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, nullable=False)
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), nullable=False)
    id_editorial = db.Column(db.Integer, db.ForeignKey('editoriales.id_editorial'),nullable=False)
    anio_publicacion = db.Column(db.String(4), nullable=False)  # o Integer si prefieres

    material = db.relationship('Material', back_populates = 'libro')
    editorial = db.relationship('Editorial', back_populates = 'libros')

    def __init__(self, isbn, id_material, id_editorial, anio_publicacion):
        self.isbn = isbn
        self.id_material= id_material
        self.id_editorial = id_editorial
        self.anio_publicacion = anio_publicacion

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, isbn=None, id_material=None, id_editorial=None, anio_publicacion=None):
        if isbn:
            self.isbn = isbn
        if id_material:
            self.id_material=id_material
        if id_editorial:
            self.id_editorial = id_editorial
        if anio_publicacion:
            self.anio_publicacion = anio_publicacion
        db.session.commit()

    @staticmethod
    def get_all():
        return Libro.query.all()

    @staticmethod
    def get_by_id(id_libro):
        return Libro.query.get(id_libro)

    def to_dict(self):
        return {
            'id_libro': self.id_libro,
            'isbn': self.isbn,
            'id_material': self.id_material,
            'id_editorial': self.id_editorial,
            'anio_publicacion': self.anio_publicacion
        }