from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario_model import Usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            session['usuario_id'] = user.id
            session['usuario_tipo'] = user.tipo
            session['usuario_nombre'] = user.nombre
            return redirect(url_for('home'))
        flash("Usuario o contraseña incorrectos")
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
