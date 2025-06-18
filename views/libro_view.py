from flask import render_template

def list(libros):
    return render_template('libros/index.html', libros=libros)

def create():
    return render_template('libros/create.html')

def edit(libro):
    return render_template('libros/edit.html', libro=libro)
