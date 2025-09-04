from flask import request, jsonify, Blueprint
from model import (TarefaNaoEncontrada, criar_tarefa, ler_tarefa, ler_tarefa_id, atualizar_tarefa, deletar_tarefa)

tarefas = Blueprint('tarefas', __name__)

@tarefas.route("/tarefas", methods = ['POST'])
def criar_tarefa():
    try:
        dados = request.json
        print(f"dados coletados: {dados}")
        resposta, status_code = criar_tarefa(dados)
        return jsonify(resposta), status_code
    
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao criar tarefa: {str(e)}'}), 500

@tarefas.route("/tarefas", methods = ['GET'])
def ler_tarefa():
    try:
        tarefas = ler_tarefa()
        return jsonify(tarefas)
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao listar tarefas: {str(e)}'}), 500

@tarefas.route('/tarefas/<int:id_tarefa>', methods = ['GET'])
def ler_tarefa_id(id_tarefa):
    try:
        tarefas = ler_tarefa_id(id_tarefa)
        return jsonify(tarefas)
    except TarefaNaoEncontrada:
        return jsonify({'erro': 'Tarefa não encontrada!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao buscar tarefa: {str(e)}'}), 500

@tarefas.route('/tarefas/<int:id_tarefa>', methods = ['PUT'])
def atualizar_tarefa(id_tarefa):
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
def deletar_tarefa(id_tarefa):
    try:
        deletar_tarefa(id_tarefa)
        return jsonify({'mensagem': 'Tarefa deletada com sucesso!'}), 200
    except TarefaNaoEncontrada:
        return jsonify({'erro': 'Tarefa não encontrada!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao deletar tarefa: {str(e)}'}), 500