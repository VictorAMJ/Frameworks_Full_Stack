import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Ativa o debug
    DEBUG = True

    # Configuração do banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'livros.db')
    
    # Evita avisos de modificações no SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

