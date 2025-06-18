from flask import render_template

def list(bibliotecarios):
    return render_template('bibliotecarios/index.html', bibliotecarios=bibliotecarios)

def create():
    return render_template('bibliotecarios/create.html')

def edit(bibliotecario):
    return render_template('bibliotecarios/edit.html', bibliotecario=bibliotecario)