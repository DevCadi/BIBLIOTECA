from flask import Blueprint, render_template, session, redirect, url_for
from models.material_model import Material

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    novedades = Material.get_recent()  # tu método para traer materiales recientes

    # Si el usuario tiene sesión y es lector
    if 'user_tipo' in session:
        if session['user_tipo'].lower() == 'lector':
            return render_template('home_lector.html', novedades=novedades, tipo='lector')
        else:
            # Si es admin o cualquier otro tipo, llevar al dashboard
            return render_template('dashboard.html')

    # Si no hay sesión, visitante ve home_lector
    return render_template('home_lector.html', novedades=novedades, tipo=None)
