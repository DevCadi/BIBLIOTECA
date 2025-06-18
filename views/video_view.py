from flask import render_template

def list(videos):
    return render_template('videos/index.html', videos=videos)

def create():
    return render_template('videos/create.html')

def edit(video):
    return render_template('videos/edit.html', video=video)