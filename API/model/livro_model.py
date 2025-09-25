from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

#db é instancia e Model é a classe pra criar as tabelas do BD
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False)
    ano_publicacao = db.Column(db.Integer, nullable = False)
    genero = db.Column(db.String(50), nullable = False)
    disponivel = db.Colmun(db.Boolean, default = True)





