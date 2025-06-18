from flask import render_template

def list(materiales):
    return render_template('materiales/index.html', materiales=materiales)

def create(categorias):
    return render_template('materiales/create.html', categorias=categorias)

def edit(material, categorias):
    return render_template('materiales/edit.html', material=material, categorias=categorias)
