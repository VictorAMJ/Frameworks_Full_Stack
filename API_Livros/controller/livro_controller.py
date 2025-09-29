#Controller = faz o CRUD direto no banco

#Recebe a requisição HTTP (ex.: POST /livros), chama a lógica no service e devolve a resposta em JSON.


from model.livro_model import Livro, db

def criar_livro(dados):
    novo_livro = Livro(
        titulo = dados['titulo'],
        autor = dados['autor'],
        ano_publicacao = dados['ano_publicacao'],
        genero = dados['genero'],
        disponivel = dados.get('disponivel', True)
    )

    db.session.add(novo_livro)
    db.session.commit()
    return novo_livro
#vai receber a requisição e devolver as respostas em json


def listar_livros():
    return Livro.query.all()

def listar_livro_id(id):
    return Livro.query.get(id)

def atualizar_livro(id, dados):
    livro = Livro.query.get(id)
    if livro:
        livro.titulo = dados.get('titulo', livro.titulo)
        livro.autor = dados.get('autor', livro.autor)
        livro.ano_publicacao = dados.get('ano_publicacao', livro.ano_publicacao)
        livro.genero = dados.get('genero', livro.genero)
        livro.disponivel = dados.get('disponivel', livro.disponivel)
        db.session.commit()
    return livro

def deletar_livro(id):
    livro = Livro.query.get(id)
    if livro:
        db.session.delete(livro)
        db.session.commit()
    return livro











