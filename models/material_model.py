from database import db

class Material(db.Model):
    __tablename__ = 'materiales'

    id_material = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    fecha_ingreso = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    id_categoria = db.Column(db.Integer, nullable=False)

    def __init__(self, tipo, titulo, fecha_ingreso, estado, id_categoria):
        self.tipo = tipo
        self.titulo = titulo
        self.fecha_ingreso = fecha_ingreso
        self.estado = estado
        self.id_categoria = id_categoria

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, tipo=None, titulo=None, fecha_ingreso=None, estado=None, id_categoria=None):
        if tipo: self.tipo = tipo
        if titulo: self.titulo = titulo
        if fecha_ingreso: self.fecha_ingreso = fecha_ingreso
        if estado: self.estado = estado
        if id_categoria: self.id_categoria = id_categoria
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Material.query.all()

    @staticmethod
    def get_by_id(id_material):
        return Material.query.get(id_material)
