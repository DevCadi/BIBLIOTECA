from database import db

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_bibliotecario = db.Column(db.Integer, nullable=False)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    def __init__(self, id_usuario, id_bibliotecario, fecha_prestamo, fecha_devolucion, estado):
        self.id_usuario = id_usuario
        self.id_bibliotecario = id_bibliotecario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, id_usuario=None, id_bibliotecario=None, fecha_prestamo=None, fecha_devolucion=None, estado=None):
        if id_usuario: self.id_usuario = id_usuario
        if id_bibliotecario: self.id_bibliotecario = id_bibliotecario
        if fecha_prestamo: self.fecha_prestamo = fecha_prestamo
        if fecha_devolucion: self.fecha_devolucion = fecha_devolucion
        if estado: self.estado = estado
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Prestamo.query.all()

    @staticmethod
    def get_by_id(id_prestamo):
        return Prestamo.query.get(id_prestamo)
    
    def to_dict(self):
        return {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_bibliotecario': self.id_bibliotecario,
            'fecha_prestamo': str(self.fecha_prestamo),
            'fecha_devolucion': str(self.fecha_devolucion),
            'estado': self.estado
        }

