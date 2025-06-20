from flask import Blueprint, render_template
from models.usuario_model import Usuario
from models.prestamo_model import Prestamo
from models.material_model import Material
from sqlalchemy import func
from database import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    total_lectores = Usuario.query.filter_by(tipo='Lector').count() or 0
    total_prestamos = Prestamo.query.count() or 0

    ranking_materiales = (
        db.session.query(Material.titulo, func.count(Prestamo.id_material))
        .join(Prestamo, Material.id_material == Prestamo.id_material)
        .group_by(Material.titulo)
        .order_by(func.count(Prestamo.id_material).desc())
        .limit(5)
        .all()
    )

    return render_template('dashboard.html',
        total_lectores=int(total_lectores),
        total_prestamos=int(total_prestamos),
        ranking_materiales=ranking_materiales
    )
