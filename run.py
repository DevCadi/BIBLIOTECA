from flask import Flask, request, render_template
<<<<<<< HEAD
from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,material_controllers, prestamo_controllers, proyectos_academicos_controllers
=======

from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,material_controllers, prestamo_controllers, proyectos_academicos_controllers

>>>>>>> dda3e7f5b6d15bc192d7bc79ac685c93cd408213
from database import db

app = Flask(__name__)

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


@app.route("/")
def home():
    return render_template("base.html") 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)