from flask import request, redirect, url_for, Blueprint
from models.material_model import  Material
from models.video_model import Video
from views import video_view

video_bp = Blueprint('video',__name__,url_prefix="/videos")

@video_bp.route("/")
def index():
    video = Video.get_all()
    return video_view.list(video)

@video_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        id_material = request.form['id_material']
        duracion = request.form['duracion']
        formato = request.form['formato']
        director = request.form['director']
    
        video = Video(id_material, duracion, formato, director)
        video.save()
        return redirect(url_for('video.index'))
    materiales = Material.query.all()
    return video_view.create(materiales=materiales)

@video_bp.route("/edit/<int:id_video>", methods=['GET','POST'])
def edit(id_video):
    video = Video.get_by_id(id_video)
    if request.method == 'POST':
        id_material = request.form['id_material']
        duracion = request.form['duracion']
        formato = request.form['formato']
        director = request.form['director']

        video.update(id_material=id_material, duracion=duracion, formato=formato, director=director)
        return redirect(url_for('video.index'))
    materiales = Material.query.all()
    return video_view.edit(video=video, materiales=materiales)

@video_bp.route("/delete/<int:id_video>")
def delete(id_video):
    video = Video.get_by_id(id_video)
    video.delete()
    return redirect(url_for('video.index'))
