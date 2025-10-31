import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'livros.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

