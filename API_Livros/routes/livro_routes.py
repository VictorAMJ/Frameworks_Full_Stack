#Routes = define as URLs e chama os métodos do controller

from flask import Blueprint, request, jsonify
from controller.livro_controller import criar_livro, listar_livros, listar_livro_id, atualizar_livro, deletar_livro

livro_bp = Blueprint("livro_bp", __name__)

@livro_bp.route("/livro", methods=["POST"])
def criar_livro_route():
    dados = request.get_json()
    livro = criar_livro(dados)
    return jsonify({"mensagem": f"Livro '{livro.titulo}' criado com sucesso!"}), 201

@livro_bp.route("/livros", methods=["GET"])
def listar_livro_route():
    livros = listar_livros()
    lista = []
    for livro in livros:
        lista.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "genero": livro.genero,
            "disponivel": livro.disponivel
        })
    return jsonify(lista), 200

@livro_bp.route("/livros/<int:id>", methods=["GET"])
def listar_livro_route_id(id):
    livro = listar_livro_id(id)
    if livro:
        return jsonify({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "ano_publicacao": livro.ano_publicacao,
            "genero": livro.genero,
            "disponivel": livro.disponivel
        }), 200
    return jsonify({"erro" : f"Livro com ID {id} não encontrado"}), 404

@livro_bp.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro_route(id):
    dados = request.get_json()
    livro = atualizar_livro(id, dados)
    if livro:
        return jsonify({"mensagem": f"Livro '{livro.titulo}' atualizado com sucesso!"}), 200
    return jsonify({"erro": f"Livro com ID {id} não encontrado"}), 404

@livro_bp.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro_route(id):
    livro = deletar_livro(id)
    if livro:
        return jsonify({"mensagem": f"Livro '{livro.titulo}' deletado com sucesso!"}), 200
    return jsonify({"erro": f"Livro com ID {id} não encontrado"}), 404
