from flask import render_template

def list(libros):
    return render_template('libros/index.html', libros=libros)

def create(materiales, editoriales):
    return render_template('libros/create.html', materiales=materiales, editoriales=editoriales)

def edit(libro, materiales, editoriales):
    return render_template('libros/edit.html', libro=libro, materiales=materiales, editoriales=editoriales)
