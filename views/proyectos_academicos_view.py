from flask import render_template

def list(proyectos):
    return render_template('proyectos_academicos/index.html', proyectos=proyectos)

def create():
    return render_template('proyectos_academicos/create.html')

def edit(proyecto):
    return render_template('proyectos_academicos/edit.html', proyecto=proyecto)