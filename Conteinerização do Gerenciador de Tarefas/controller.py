from flask import request, jsonify, Blueprint
from model import TarefaNaoEncontrada, criar_tarefa, ler_tarefa, ler_tarefa_id, atualizar_tarefa, deletar_tarefa

tarefas = Blueprint('tarefas', __name__)

@tarefas.route("/tarefas", methods = ['POST'])
def criar_tarefa():
    """
    Cria uma nova tarefa
    ---
    tags:
      - Tasks
    description: Cria uma nova tarefa; o usuário pode inserir o título, a descrição e o status da tarefa.
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - titulo
            - id_usuario
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            id_usuario:
              type: integer
    responses:
      201:
        description: Tarefa criada com sucesso!
        schema:
          type: object
          properties:
            mensagem:
              type: string
    """
    try:
        dados = request.json
        print(f"dados coletados: {dados}")
        resposta, status_code = criar_tarefa(dados)
        return jsonify(resposta), status_code
    
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao criar tarefa: {str(e)}'}), 500

@tarefas.route("/tarefas", methods = ['GET'])
def get_ler_tarefa():
    """
    Lista as tarefas inseridas
    ---
    tags:
      - Tasks
    description: Exibe em forma de lista todas as tarefas e seus status.
    responses:
      200:
        description: Lista de tarefas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              titulo:
                type: string
              descricao:
                type: string
              status:
                type: string
              id_usuario:
                type: integer
    """
    try:
        tarefas = ler_tarefa()
        return jsonify(tarefas)
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao listar tarefas: {str(e)}'}), 500

@tarefas.route('/tarefas/<int:id_tarefa>', methods = ['GET'])
def get_ler_tarefa_id(id_tarefa):
    """
    Retorna uma tarefa específica
    ---
    tags:
      - Tasks
    description: Exibe apenas a tarefa com o ID especificado e seu status.
    parameters:
      - in: path
        name: id_tarefa
        type: integer
        required: true
        description: ID da tarefa a ser exibida
    responses:
      200:
        description: Tarefa encontrada
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            id_usuario:
              type: integer
      404:
        description: Tarefa não encontrada
        schema:
          type: object
          properties:
            erro:
              type: string
    """
    try:
        tarefas = ler_tarefa_id(id_tarefa)
        return jsonify(tarefas)
    except TarefaNaoEncontrada:
        return jsonify({'erro': 'Tarefa não encontrada!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao buscar tarefa: {str(e)}'}), 500

@tarefas.route('/tarefas/<int:id_tarefa>', methods = ['PUT'])
def upd_atualizar_tarefa(id_tarefa):
    """
    Atualiza uma tarefa
    ---
    tags:
      - Tasks
    description: Atualiza os dados de uma tarefa, incluindo título, descrição e status.
    parameters:
      - in: path
        name: id_tarefa
        type: integer
        required: true
        description: ID da tarefa que será atualizada
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            id_usuario:
              type: integer
    responses:
      200:
        description: Tarefa atualizada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            id_usuario:
              type: integer
      404:
        description: Tarefa não encontrada
        schema:
          type: object
          properties:
            erro:
              type: string
    """
    dados = request.json
    try:
        tarefas = atualizar_tarefa(id_tarefa, dados)
        if not tarefas:
            return jsonify({'erro': 'Tarefa não encontrada!'}), 404
        atualizar_tarefa(id_tarefa,dados)
        return jsonify(dados), 200
    except TarefaNaoEncontrada:
        return jsonify({'erro': 'Tarefa não encontrada!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao atualizar tarefa: {str(e)}'}), 500
    
@tarefas.route('/tarefas/<int:id_tarefas>', methods = ['DELETE'])
def del_deletar_tarefa(id_tarefa):
    """
    Deleta uma tarefa
    ---
    tags:
      - Tasks
    description: Remove uma tarefa do banco de dados.
    parameters:
      - in: path
        name: id_tarefa
        type: integer
        required: true
        description: ID da tarefa que será deletada
    responses:
      200:
        description: Tarefa deletada com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
      404:
        description: Tarefa não encontrada
        schema:
          type: object
          properties:
            erro:
              type: string
    """
    try:
        deletar_tarefa(id_tarefa)
        return jsonify({'mensagem': 'Tarefa deletada com sucesso!'}), 200
    except TarefaNaoEncontrada:
        return jsonify({'erro': 'Tarefa não encontrada!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao deletar tarefa: {str(e)}'}), 500