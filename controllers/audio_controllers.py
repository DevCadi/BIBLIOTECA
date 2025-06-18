from flask import request, redirect, url_for, Blueprint

from models.audio_model import Audio
from views import audio_view

audio_bp = Blueprint('audio',__name__,url_prefix="/audios")

@audio_bp.route("/")
def index():
    audio = Audio.get_all()
    return audio_view.list(audio)

@audio_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        duracion = request.form['duracion']
        formato = request.form['formato']
        propietario = request.form['duracion']
    
        audio = Audio(duracion, formato, propietario)
        audio.save()
        return redirect(url_for('audio.index'))
    return audio_view.create()

@audio_bp.route("/edit/<int:id_audio>", methods=['GET','POST'])
def edit(id_audio):
    audio = Audio.get_by_id(id_audio)
    if request.method == 'POST':
        duracion = request.form['duracion']
        formato = request.form['formato']
        propietario = request.form['duracion']

        audio.update(duracion=duracion, formato=formato, propietario=propietario)
        return redirect(url_for('audio.index'))
    return audio_view.edit(audio)

@audio_bp.route("/delete/<int:id_audio>")
def delete(id_audio):
    audio = Audio.get_by_id(id_audio)
    audio.delete()
    return redirect(url_for('audio.index'))
