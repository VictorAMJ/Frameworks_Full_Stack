from flask import Flask
from config import Config
from routes.livro_routes import livro_bp
from model.livro_model import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(livro_bp)

@app.route("/")
def index():
    return "API de Livros funcionando!"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)










