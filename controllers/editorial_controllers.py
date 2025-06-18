from flask import request, redirect, url_for, Blueprint

from models.editorial_model import  Editorial
from views import editorial_view

editorial_bp = Blueprint('editorial',__name__,url_prefix="/editoriales")

@editorial_bp.route("/")
def index():
    editorial = Editorial.get_all()
    return editorial_view.list(editorial)

@editorial_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais = request.form['pais']
    
        editorial = Editorial(nombre, pais)
        editorial.save()
        return redirect(url_for('editorial.index'))
    return editorial_view.create()

@editorial_bp.route("/edit/<int:id_editorial>", methods=['GET','POST'])
def edit(id_editorial):
    editorial = Editorial.get_by_id(id_editorial)
    if request.method == 'POST':
        nombre = request.form['nombre']
        pais = request.form['pais']

        editorial.update(nombre=nombre, pais=pais)
        return redirect(url_for('editorial.index'))
    return editorial_view.edit(editorial)

@editorial_bp.route("/delete/<int:id_editorial>")
def delete(id_editorial):
    editorial = Editorial.get_by_id(id_editorial)
    editorial.delete()
    return redirect(url_for('editorial.index'))
