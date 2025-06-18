from flask import render_template

def list(materiales):
    return render_template('materiales/index.html', materiales=materiales)

def create():
    return render_template('materiales/create.html')

def edit(material):
    return render_template('materiales/edit.html', material=material)
