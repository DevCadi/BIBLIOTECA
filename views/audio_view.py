from flask import render_template

def list(audios):
    return render_template('audios/index.html', audios=audios)

def create():
    return render_template('audios/create.html')

def edit(audio):
    return render_template('audios/edit.html', audio=audio)