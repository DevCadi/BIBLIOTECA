from flask import request, redirect, url_for, Blueprint
from models.material_model import Material
from models.categoria_model import Categoria
from models.autores_model import Autores
from views import categoria_view
from views import material_view

material_bp = Blueprint('material', __name__, url_prefix='/materiales')

@material_bp.route("/")
def index():
    materiales = Material.get_all()
    return material_view.list(materiales)

@material_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        fecha_ingreso = request.form['fecha_ingreso']
        estado = request.form['estado']
        id_categoria = request.form['id_categoria']
        id_autor = request.form['id_autor']

        material = Material(tipo, titulo, fecha_ingreso, estado, id_categoria, id_autor)
        material.save()
        return redirect(url_for('material.index'))
    categorias = Categoria.query.all()
    autores = Autores.query.all()

    return material_view.create(categorias=categorias, autores=autores)

@material_bp.route("/edit/<int:id_material>", methods=['GET', 'POST'])
def edit(id_material):
    material = Material.get_by_id(id_material)
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        fecha_ingreso = request.form['fecha_ingreso']
        estado = request.form['estado']
        id_categoria = request.form['id_categoria']
        id_autor = request.form['id_autor']

        material.update(tipo=tipo, titulo=titulo, fecha_ingreso=fecha_ingreso, estado=estado, id_categoria=id_categoria, id_autor=id_autor)
        return redirect(url_for('material.index'))

    categorias = Categoria.query.all()
    autores = Autores.query.all()

    return material_view.edit(material=material, categorias=categorias, autores=autores)

@material_bp.route("/delete/<int:id_material>")
def delete(id_material):
    material = Material.get_by_id(id_material)
    material.delete()
    return redirect(url_for('material.index'))
