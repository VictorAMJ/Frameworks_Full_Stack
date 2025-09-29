#Model = define tabela do banco

#Representa os dados e como eles ficam no banco.
#Classe Livro que vira tabela livros no SQLite
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

#db é instancia e Model é a classe pra criar as tabelas do BD
class Livro(db.Model):
    __tablename__ = "livros"
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False)
    ano_publicacao = db.Column(db.Integer, nullable = False)
    genero = db.Column(db.String(50), nullable = False)
    disponivel = db.Column(db.Boolean, default = True)





