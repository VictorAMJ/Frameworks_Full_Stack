#Routes = define as URLs e chama os métodos do controller

from flask import Blueprint, request, jsonify
from controller.livro_controller import criar_livro, listar_livros, listar_livro_id, atualizar_livro, deletar_livro

livro_bp = Blueprint("livro_bp", __name__)

@livro_bp.route("/livro", methods=["POST"])
def criar_livro_route():
    """
    Criar um novo livro
    ---
    tags:
      - Livros
    parameters:
      - in: body
        name: body
        required: true
        description: Dados do novo livro
        schema:
          type: object
          required:
            - titulo
            - autor
            - ano_publicacao
            - genero
          properties:
            titulo:
              type: string
              example: "Batman: O Cavaleiro das Trevas"
            autor:
              type: string
              example: "Frank Miller"
            ano_publicacao:
              type: integer
              example: 1954
            genero:
              type: string
              example: Ação
            disponivel:
              type: boolean
              example: true
    responses:
      201:
        description: Livro criado com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Livro 'Batman: O Cavaleiro das Trevas' criado com sucesso!"
    """
    dados = request.get_json()
    livro = criar_livro(dados)
    return jsonify({"mensagem": f"Livro '{livro.titulo}' criado com sucesso!"}), 201

@livro_bp.route("/livros", methods=["GET"])
def listar_livro_route():
    """
    Listar todos os livros
    ---
    tags:
      - Livros
    responses:
      200:
        description: Lista de livros
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              autor:
                type: string
              ano_publicacao:
                type: integer
              genero:
                type: string
              disponivel:
                type: boolean
    """
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
    """
    Buscar um livro pelo ID
    ---
    tags:
      - Livros
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do livro
    responses:
      200:
        description: Livro encontrado
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            autor:
              type: string
            ano_publicacao:
              type: integer
            genero:
              type: string
            disponivel:
              type: boolean
      404:
        description: Livro não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: "Livro com ID 1 não encontrado"
    """
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
    """
    Atualizar um livro existente
    ---
    tags:
      - Livros
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do livro a ser atualizado
      - in: body
        name: body
        required: true
        description: Dados do livro a serem atualizados
        schema:
          type: object
          properties:
            titulo:
              type: string
              example: "Novo Título"
            autor:
              type: string
              example: "Novo Autor"
            ano_publicacao:
              type: integer
              example: 2025
            genero:
              type: string
              example: "Fantasia"
            disponivel:
              type: boolean
              example: true
    responses:
      200:
        description: Livro atualizado com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Livro 'Novo Título' atualizado com sucesso!"
      404:
        description: Livro não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: "Livro com ID 1 não encontrado"
    """
    dados = request.get_json()
    livro = atualizar_livro(id, dados)
    if livro:
        return jsonify({"mensagem": f"Livro '{livro.titulo}' atualizado com sucesso!"}), 200
    return jsonify({"erro": f"Livro com ID {id} não encontrado"}), 404

@livro_bp.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro_route(id):
    """
    Deletar um livro pelo ID
    ---
    tags:
      - Livros
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do livro a ser deletado
    responses:
      200:
        description: Livro deletado com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Livro 'Título do Livro' deletado com sucesso!"
      404:
        description: Livro não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: "Livro com ID 1 não encontrado"
    """
    livro = deletar_livro(id)
    if livro:
        return jsonify({"mensagem": f"Livro '{livro.titulo}' deletado com sucesso!"}), 200
    return jsonify({"erro": f"Livro com ID {id} não encontrado"}), 404
