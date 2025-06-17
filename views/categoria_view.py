from flask import render_template

def list(categorias):
    return render_template('categorias/index.html', categorias=categorias)

def create():
    return render_template('categorias/create.html')

def edit(categoria):
    return render_template('categorias/edit.html', categoria=categoria)