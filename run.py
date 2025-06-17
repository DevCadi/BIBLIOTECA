from flask import Flask, request
from controllers import categoria_controllers
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(categoria_controllers.Categoria)

@app.route("/")
def home():
    return "<h1>Aplicación Biblioteca</h1>"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)