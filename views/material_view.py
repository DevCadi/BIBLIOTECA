from flask import render_template

def list(materiales):
    return render_template('materiales/index.html', materiales=materiales)

def create(materiales, categoria):
    return render_template('materiales/create.html', materiales=materiales, categoria=categoria)

def edit(material, materiales, categoria):
    return render_template('materiales/edit.html', material=material, materiales=materiales, categoria=categoria)
