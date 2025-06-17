from flask import request, redirect, url_for, Blueprint

from models.categoria_model import Categoria
from views import categoria_view

categoria_bp = Blueprint('categoria',__name__,url_prefix="/categorias")

@categoria_bp.route("/")
def index():
    categorias = Categoria.get_all()
    return categoria_view.list(categorias)

@categoria_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
    
        categoria = Categoria(nombre)
        categoria.save()
        return redirect(url_for('categoria.index'))
    return categoria_view.create()

@categoria_bp.route("/edit/<int:id_cat>", methods=['GET','POST'])
def edit(id_cat):
    categoria = Categoria.get_by_id(id_cat)
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria.update(nombre=nombre)
        return redirect(url_for('categoria.index'))
    return categoria_view.edit(categoria)

@categoria_bp.route("/delete/<int:id_cat>")
def delete(id_cat):
    categoria = Categoria.get_by_id(id_cat)
    categoria.delete()
    return redirect(url_for('categoria.index'))
