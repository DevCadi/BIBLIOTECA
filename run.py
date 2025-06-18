from flask import Flask, request, render_template
<<<<<<< HEAD
<<<<<<< HEAD

from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers


=======
from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers
>>>>>>> bc2b6ceea71b9928855bd3099066fd2d53a6d500
=======


from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,material_controllers 
>>>>>>> 6088790fab07f80b5234a39436f5817c8552b47c
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
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> bc2b6ceea71b9928855bd3099066fd2d53a6d500

=======
app.register_blueprint(material_controllers.material_bp)

>>>>>>> 6088790fab07f80b5234a39436f5817c8552b47c

@app.route("/")
def home():
    return render_template("base.html") 

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)