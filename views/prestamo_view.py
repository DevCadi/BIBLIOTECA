from flask import render_template

def list(prestamos, usuarios):
    return render_template("prestamos/index.html", prestamos=prestamos, usuarios=usuarios)

def create(usuarios, materiales):
    return render_template("prestamos/create.html", usuarios=usuarios, materiales=materiales)

def edit(prestamo, usuarios, materiales):
    return render_template("prestamos/edit.html", prestamo=prestamo, usuarios=usuarios, materiales=materiales)
