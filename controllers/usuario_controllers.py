from flask import request, redirect, url_for, Blueprint, session, abort
from utils.decorators import login_required, role_required

from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")


@usuario_bp.route("/")

def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)


@usuario_bp.route("/create", methods=['GET', 'POST'])
@login_required
@role_required('Admin')  # Solo admin puede crear
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        username = request.form['username']
        password = request.form['password']
        tipo = request.form['tipo']

        usuario = Usuario(nombre, apellido, email, telefono, username, password, tipo)
        usuario.save()
        return redirect(url_for('usuario.index'))
    return usuario_view.create()


@usuario_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
@role_required('Admin', 'Bibliotecario')
def edit(id):
    usuario = Usuario.get_by_id(id)

    # Solo admin puede editar todo; bibliotecario solo puede editar lectores
    if session['tipo'] == 'Bibliotecario' and usuario.tipo != 'Lector':
        abort(403)  # Prohibido

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        username = request.form['username']
        password = request.form['password']
        tipo = request.form['tipo']

        # Verificación para que bibliotecario no pueda cambiar el tipo a admin o bibliotecario
        if session['tipo'] == 'Bibliotecario' and tipo != 'Lector':
            abort(403)

        usuario.update(nombre=nombre, apellido=apellido, email=email,
                       telefono=telefono, username=username, password=password, tipo=tipo)
        return redirect(url_for('usuario.index'))

    return usuario_view.edit(usuario)


@usuario_bp.route("/delete/<int:id>")
@login_required
@role_required('Admin', 'Bibliotecario')
def delete(id):
    usuario = Usuario.get_by_id(id)

    # Solo admin puede eliminar admin o bibliotecario
    if session['tipo'] == 'Bibliotecario' and usuario.tipo != 'Lector':
        abort(403)

    usuario.delete()
    return redirect(url_for('usuario.index'))
