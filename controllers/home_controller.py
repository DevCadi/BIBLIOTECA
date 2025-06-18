from flask import Blueprint, render_template, session
from models.material_model import Material

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    novedades = Material.get_recent()  # suponiendo que creas este método
    return render_template('home.html', novedades=novedades, tipo=session.get('user_tipo'))
