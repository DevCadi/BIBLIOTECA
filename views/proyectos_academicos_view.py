from flask import render_template

def list(proyectos):
    return render_template('proyectos_academicos/index.html', proyectos=proyectos)

def create(materiales):
    return render_template('proyectos_academicos/create.html', materiales=materiales)

def edit(proyecto, materiales):
    return render_template('proyectos_academicos/edit.html', proyecto=proyecto, materiales=materiales)