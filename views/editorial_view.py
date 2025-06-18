from flask import render_template

def list(editoriales):
    return render_template('editoriales/index.html', editoriales=editoriales)

def create():
    return render_template('editoriales/create.html')

def edit(editorial):
    return render_template('editoriales/edit.html', editorial=editorial)