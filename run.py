<<<<<<< HEAD
from flask import Flask, request
from controllers import categoria_controllers, autores_controllers
=======
from flask import Flask, request, render_template
from controllers import categoria_controllers
from controllers import usuario_controllers
>>>>>>> 53fb63521f4130f21b4e45c5eed3a086181176d6
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuario_controllers.usuario_bp)

app.register_blueprint(categoria_controllers.categoria_bp)
app.register_blueprint(autores_controllers.autor_bp)


@app.route("/")
def home():
    return render_template("")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)