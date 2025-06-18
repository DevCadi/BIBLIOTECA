from flask import request, redirect, url_for, Blueprint

from models.autores_model import Autores
from views import autores_view

autor_bp= Blueprint('autores',__name__,url_prefix="/autores")

@autor_bp.route("/")
def index():
    #recupera todos los registros de la tabla autor en forma de objeto
    autores = Autores.get_all()
    return autores_view.list(autores)

@autor_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']

        autor = Autores(nombre)
        autor.save()
        return redirect(url_for('autores.index'))
    return autores_view.create()

@autor_bp.route("/edit/<int:id_autor>", methods = ['GET','POST'])
def edit(id_autor):
    autor = Autores.get_by_id(id_autor)
    if request.method == 'POST':
        nombre = request.form['nombre']
        #actualizar
        autor.update(nombre=nombre)
        return redirect(url_for('autores.index'))
    
    return autores_view.edit(autor)

@autor_bp.route("/delete/<int:id_autor>")
def delete(id_autor):
    autor = Autores.get_by_id(id_autor)
    autor.delete()
    return redirect(url_for('autores.index'))