from flask import request, redirect, url_for, Blueprint

from models.proyectos_academicos_model import  Proyecto
from views import proyectos_academicos_view

proyecto_bp = Blueprint('proyecto',__name__,url_prefix="/proyectos")

@proyecto_bp.route("/")
def index():
    proyectos = Proyecto.get_all()
    return proyectos_academicos_view.list(proyectos)

@proyecto_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        autor_est = request.form['autor_est']
        anio_defensa = request.form['anio_defensa']
    
        proyecto = Proyecto(autor_est, anio_defensa)
        proyecto.save()
        return redirect(url_for('proyecto.index'))
    return proyectos_academicos_view.create()

@proyecto_bp.route("/edit/<int:id_pro>", methods=['GET','POST'])
def edit(id_pro):
    proyecto = Proyecto.get_by_id(id_pro)
    if request.method == 'POST':
        autor_est = request.form['autor_est']
        anio_defensa = request.form['anio_defensa']

        proyecto.update(autor_est=autor_est, anio_defensa=anio_defensa)
        return redirect(url_for('proyecto.index'))
    return proyectos_academicos_view.edit(proyecto)

@proyecto_bp.route("/delete/<int:id_pro>")
def delete(id_pro):
    proyecto = Proyecto.get_by_id(id_pro)
    proyecto.delete()
    return redirect(url_for('proyecto.index'))
