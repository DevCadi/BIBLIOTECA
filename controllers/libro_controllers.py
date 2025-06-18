from flask import request, redirect, url_for, Blueprint
from models.libro_model import Libro
from views import libro_view

libro_bp = Blueprint('libro', __name__, url_prefix='/libros')

@libro_bp.route("/")
def index():
    libros = Libro.get_all()
    return libro_view.list(libros)

@libro_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        isbn = request.form['isbn']
        id_editorial = request.form['id_editorial']
        anio_publicacion = request.form['anio_publicacion']

        libro = Libro(isbn, id_editorial, anio_publicacion)
        libro.save()
        return redirect(url_for('libro.index'))

    return libro_view.create()

@libro_bp.route("/edit/<int:id_libro>", methods=['GET', 'POST'])
def edit(id_libro):
    libro = Libro.get_by_id(id_libro)
    if request.method == 'POST':
        isbn = request.form['isbn']
        id_editorial = request.form['id_editorial']
        anio_publicacion = request.form['anio_publicacion']
        libro.update(isbn=isbn, id_editorial=id_editorial, anio_publicacion=anio_publicacion)
        return redirect(url_for('libro.index'))

    return libro_view.edit(libro)

@libro_bp.route("/delete/<int:id_libro>")
def delete(id_libro):
    libro = Libro.get_by_id(id_libro)
    libro.delete()
    return redirect(url_for('libro.index'))
