from flask import request, redirect, url_for, Blueprint, session, abort, render_template
from utils.decorators import login_required, role_required
from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")

# ----------- LOGIN -----------
@usuario_bp.route("login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.verify_password(password):
            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            session['usuario_tipo'] = usuario.tipo
            return redirect(url_for('home'))  # redirige al home principal
        else:
            return "Credenciales incorrectas", 401

    return usuario_view.login()

@usuario_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

# ----------- CRUD USUARIOS -----------

@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods=['GET', 'POST'])
@login_required
@role_required('Admin')
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

    if session['usuario_tipo'] == 'Bibliotecario' and usuario.tipo != 'Lector':
        abort(403)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        username = request.form['username']
        password = request.form['password']
        tipo = request.form['tipo']

        if session['usuario_tipo'] == 'Bibliotecario' and tipo != 'Lector':
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

    if session['usuario_tipo'] == 'Bibliotecario' and usuario.tipo != 'Lector':
        abort(403)

    usuario.delete()
    return redirect(url_for('usuario.index'))
