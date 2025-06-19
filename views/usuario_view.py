from flask import render_template

def list(usuarios):
    return render_template('usuarios/index.html', usuarios=usuarios)

def create():
    return render_template('usuarios/create.html')

def edit(usuario):
    return render_template('usuarios/edit.html', usuario=usuario)

def login():
    return render_template('auth/login.html')
