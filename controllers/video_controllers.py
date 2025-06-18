from flask import request, redirect, url_for, Blueprint

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
        duracion = request.form['duracion']
        formato = request.form['formato']
        director = request.form['duracion']
    
        video = Video(duracion, formato, director)
        video.save()
        return redirect(url_for('video.index'))
    return video_view.create()

@video_bp.route("/edit/<int:id_video>", methods=['GET','POST'])
def edit(id_video):
    video = Video.get_by_id(id_video)
    if request.method == 'POST':
        duracion = request.form['duracion']
        formato = request.form['formato']
        director = request.form['duracion']

        video.update(duracion=duracion, formato=formato, director=director)
        return redirect(url_for('video.index'))
    return video_view.edit(video)

@video_bp.route("/delete/<int:id_video>")
def delete(id_video):
    video = Video.get_by_id(id_video)
    video.delete()
    return redirect(url_for('video.index'))
