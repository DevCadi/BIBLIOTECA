from flask import render_template

def list(proyectos):
    return render_template('proyectos/index.html', proyectos=proyectos)

def create():
    return render_template('proyectos/create.html')

def edit(proyecto):
    return render_template('proyectos/edit.html', proyecto=proyecto)