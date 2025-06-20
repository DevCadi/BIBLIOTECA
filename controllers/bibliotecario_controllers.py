from flask import request, redirect, url_for, Blueprint, render_template,flash

from models.bibliotecario_model import  Bibliotecario
from views import bibliotecario_view
from models.usuario_model import Usuario

bibliotecario_bp = Blueprint('bibliotecario',__name__,url_prefix="/bibliotecarios")

@bibliotecario_bp.route("/")
def index():
    bibliotecario = Bibliotecario.get_all()
    return bibliotecario_view.list(bibliotecario)

@bibliotecario_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        turno = request.form['turno']
        fecha_contratacion = request.form['fecha_contratacion']
        id_usuario = request.form['id_usuario']

        nuevo_biblio = Bibliotecario(turno, fecha_contratacion, id_usuario)
        nuevo_biblio.save()
        flash("Bibliotecario registrado exitosamente.")
        return redirect(url_for('bibliotecario.index'))

    # Filtrar usuarios con tipo 'Bibliotecario'
    usuarios_biblio = Usuario.query.filter_by(tipo='Bibliotecario').all()
    return render_template('bibliotecarios/create.html', usuarios=usuarios_biblio)


@bibliotecario_bp.route("/edit/<int:id_biblio>", methods=['GET','POST'])
def edit(id_biblio):
    bibliotecario = Bibliotecario.get_by_id(id_biblio)
    if request.method == 'POST':
        turno = request.form['turno']
        fecha_contratacion = request.form['fecha_contratacion']

        bibliotecario.update(turno=turno, fecha_contratacion=fecha_contratacion)
        return redirect(url_for('bibliotecario.index'))
    return bibliotecario_view.edit(bibliotecario)

@bibliotecario_bp.route("/delete/<int:id_biblio>")
def delete(id_biblio):
    bibliotecario = Bibliotecario.get_by_id(id_biblio)
    bibliotecario.delete()
    return redirect(url_for('bibliotecario.index'))
