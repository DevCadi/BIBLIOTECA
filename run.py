from flask import Flask, request, render_template, session, redirect, url_for

from models.material_model import Material
from models.usuario_model import Usuario

from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,material_controllers, prestamo_controllers, proyectos_academicos_controllers, auth_controllers, reporte_controllers

from database import db

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_segura'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

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

from flask import render_template, request, session
from models.material_model import Material

from flask import render_template, request, session
from models.material_model import Material
from sqlalchemy import or_

@app.route("/")
def home():
    tipo = request.args.get("tipo")
    buscar = request.args.get("buscar")

    query = Material.query

    # Filtro por tipo si se envió
    if tipo:
        if tipo.lower() == 'proyecto':
            # Mostrar materiales que tengan "proyecto" o "tesis" en el tipo
            query = query.filter(
                or_(
                    Material.tipo.ilike('%proyecto%'),
                    Material.tipo.ilike('%tesis%')
                )
            )
        else:
            query = query.filter(Material.tipo.ilike(f"%{tipo}%"))

    # Filtro por búsqueda en el título si se envió
    if buscar:
        query = query.filter(Material.titulo.ilike(f"%{buscar}%"))

    materiales = query.all()

    # Si hay sesión y el usuario es lector, mostrar home_lector
    if 'usuario_tipo' in session and session['usuario_tipo'].lower() == 'lector':
        return render_template('home_lector.html', materiales=materiales)

    # Si hay sesión pero no es lector, mostrar dashboard
    elif 'usuario_tipo' in session:
        return render_template('dashboard.html')

    # Si no hay sesión, mostrar home_lector como visitante
    return render_template('home_lector.html', materiales=materiales)

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