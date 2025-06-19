from flask import render_template

def list(audios):
    return render_template('audios/index.html', audios=audios)

def create(materiales):
    return render_template('audios/create.html', materiales=materiales)

def edit(audio, materiales):
    return render_template('audios/edit.html', audio=audio, materiales=materiales)