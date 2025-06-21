from flask import Flask, request, render_template, session, redirect, url_for
from sqlalchemy import or_
from models.material_model import Material
from models.usuario_model import Usuario
from database import db

from controllers.dashboard_controllers import dashboard_bp
from controllers import (
    categoria_controllers, autores_controllers, usuario_controllers, audio_controllers,
    bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,
    material_controllers, prestamo_controllers, proyectos_academicos_controllers,
    auth_controllers, reporte_controllers
)

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_segura'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Registrar blueprints
app.register_blueprint(audio_controllers.audio_bp)
app.register_blueprint(usuario_controllers.usuario_bp)
app.register_blueprint(bibliotecario_controllers.bibliotecario_bp)
app.register_blueprint(categoria_controllers.categoria_bp)
app.register_blueprint(autores_controllers.autor_bp)
app.register_blueprint(editorial_controllers.editorial_bp)
app.register_blueprint(video_controllers.video_bp)
app.register_blueprint(libro_controllers.libro_bp)
app.register_blueprint(material_controllers.material_bp)
app.register_blueprint(prestamo_controllers.prestamo_bp)
app.register_blueprint(proyectos_academicos_controllers.proyecto_bp)
app.register_blueprint(auth_controllers.auth_bp)
app.register_blueprint(reporte_controllers.reporte_bp)
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route("/")
def home():
    tipo = request.args.get("tipo")
    buscar = request.args.get("buscar")

    query = Material.query

    if tipo:
        if tipo.lower() == 'proyecto':
            query = query.filter(
                or_(
                    Material.tipo.ilike('%proyecto%'),
                    Material.tipo.ilike('%tesis%')
                )
            )
        else:
            query = query.filter(Material.tipo.ilike(f"%{tipo}%"))

    if buscar:
        query = query.filter(Material.titulo.ilike(f"%{buscar}%"))

    materiales = query.all()

    # Redirección lógica corregida
    if 'usuario_tipo' in session:
        if session['usuario_tipo'].lower() == 'lector':
            return render_template('home_lector.html', materiales=materiales)
        else:
            return render_template('dashboard.html')

    return render_template('home_lector.html', materiales=materiales)

# Crear admin inicial si no existe
def crear_admin_inicial():
    admin_existente = Usuario.query.filter_by(tipo="Admin").first()
    if not admin_existente:
        admin = Usuario(
            nombre="Genesis",
            apellido="Campos",
            email="genesis@gmail.com",
            telefono="77587271",
            username="admin",
            password="123",
            tipo="Admin"
        )
        admin.save()
        print("Usuario Admin creado automáticamente.")
    else:
        print("Usuario Admin ya existe.")

@app.route('/carrera')
def carrera():
    return render_template('carrera.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_admin_inicial()
    app.run(debug=True)
