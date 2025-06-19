from flask import render_template

def list(videos):
    return render_template('videos/index.html', videos=videos)

def create(materiales):
    return render_template('videos/create.html', materiales=materiales)

def edit(video, materiales):
    return render_template('videos/edit.html', video=video, materiales=materiales)