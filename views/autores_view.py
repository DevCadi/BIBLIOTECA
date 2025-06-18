from flask import render_template

def list(autores):
    return render_template('autores/index.html', autores=autores)

def create():
    return render_template('autores/create.html')

def edit(autores):
    return render_template('autores/edit.html', autores=autores)