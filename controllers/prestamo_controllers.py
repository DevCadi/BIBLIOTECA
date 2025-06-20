from flask import request, redirect, url_for, Blueprint
from datetime import datetime
from models.prestamo_model import Prestamo
from models.usuario_model import Usuario
from views import prestamo_view
from models.material_model import Material


prestamo_bp = Blueprint('prestamo', __name__, url_prefix="/prestamos")

@prestamo_bp.route("/")
def index():
    prestamos = Prestamo.get_all()
    usuarios = Usuario.get_all()
    materiales = Material.get_all()
    return prestamo_view.list(prestamos, usuarios, materiales)

@prestamo_bp.route("/create", methods=['GET', 'POST'])
def create():
    usuarios = Usuario.get_all()
    materiales = Material.get_all()

    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_bibliotecario = request.form['id_bibliotecario']
        id_material = request.form['id_material']  
        fecha_prestamo = datetime.strptime(request.form['fecha_prestamo'], "%Y-%m-%d").date()
        fecha_devolucion = datetime.strptime(request.form['fecha_devolucion'], "%Y-%m-%d").date()
        estado = request.form['estado']

        prestamo = Prestamo(
            id_usuario=id_usuario,
            id_bibliotecario=id_bibliotecario,
            id_material=id_material,  
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion=fecha_devolucion,
            estado=estado
        )
        prestamo.save()
        return redirect(url_for('prestamo.index'))

    return prestamo_view.create(usuarios, materiales)


@prestamo_bp.route("/edit/<int:id_prestamo>", methods=['GET', 'POST'])
def edit(id_prestamo):
    prestamo = Prestamo.get_by_id(id_prestamo)
    usuarios = Usuario.get_all()
    materiales = Material.get_all()  # <-- Falta esta línea para obtener los materiales

    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_bibliotecario = request.form['id_bibliotecario']
        id_material = request.form['id_material'] 
        fecha_prestamo = datetime.strptime(request.form['fecha_prestamo'], "%Y-%m-%d").date()
        fecha_devolucion = datetime.strptime(request.form['fecha_devolucion'], "%Y-%m-%d").date()
        estado = request.form['estado']

        prestamo.update(id_usuario=id_usuario, id_bibliotecario=id_bibliotecario, id_material=id_material,
                        fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion,
                        estado=estado)
        return redirect(url_for('prestamo.index'))

    # Aquí debes pasar la variable materiales también
    return prestamo_view.edit(prestamo, usuarios, materiales)


@prestamo_bp.route("/delete/<int:id_prestamo>")
def delete(id_prestamo):
    
    prestamo = Prestamo.get_by_id(id_prestamo)
    prestamo.delete()
    
    return redirect(url_for('prestamo.index'))
