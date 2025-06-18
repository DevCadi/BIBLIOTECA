from flask import Flask, request, render_template
<<<<<<< HEAD
from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, video_controllers
=======
from controllers import categoria_controllers, autores_controllers, usuario_controllers, audio_controllers, bibliotecario_controllers, editorial_controllers, libro_controllers
>>>>>>> 2acc5a907f49107689aae3b4eee199d12ee84fe8
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
<<<<<<< HEAD
app.register_blueprint(video_controllers.video_bp)
=======
app.register_blueprint(libro_controllers.libro_bp)
>>>>>>> 2acc5a907f49107689aae3b4eee199d12ee84fe8


#@app.route("/")
#def home():
#    return render_template("")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)