from flask import request, redirect, url_for, Blueprint

from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuario',__name__,url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    #recupera todos los registros de la tabla usuario en forma de objeto
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods = ['GET','POST'])
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

@usuario_bp.route("/edit/<int:id>", methods = ['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        username = request.form['username']
        password = request.form['password']
        tipo = request.form['tipo']
        #actualizar
        usuario.update(nombre=nombre, apellido=apellido, email=email, telefono=telefono, username=username, password=password, tipo=tipo)
        return redirect(url_for('usuario.index'))
    
    return usuario_view.edit(usuario)

@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))