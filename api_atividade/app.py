from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        "id": 1,
        "nome": "Victor",
        "email": "victor@gmail.com"
    },
    {
        "id": 2,
        "nome": "teste",
        "email": "teste@gmail.com"
    }
]

@app.route("/usuario", methods=["POST"])
def criar_usuario():
    novo_usuario = request.json
    for usuario in usuarios:
        if usuario['id'] == novo_usuario["id"]:
            return jsonify({"erro": "ID já existente."}), 400
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201



@app.route("/usuario", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)


@app.route("/usuario/<int:idUsuario>", methods=["GET"])
def listar_usuarios_id(idUsuario):
    for usuario in usuarios:
        if usuario['id'] == idUsuario:
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado."}), 404



@app.route("/usuario/<int:idUsuario>", methods=["PUT"])
def atualizar_usuario(idUsuario):
    for usuario in usuarios:
        if usuario['id'] == idUsuario:
            usuario_existente = request.json

            usuario["id"] = usuario_existente["id"]
            usuario["nome"] = usuario_existente["nome"]
            usuario["email"] = usuario_existente["email"]

            return jsonify(usuario_existente)
    return jsonify({"erro": "Não foi possível atualizar o usuário."}), 404



@app.route("/usuario/<int:idUsuario>" , methods=["DELETE"])
def deletar_usuario(idUsuario):
    for usuario in usuarios:
        if usuario['id'] == idUsuario:
            usuario["id"].remove(usuario)
            return jsonify({"mensagem": "Usuário deletado com sucesso!"}), 200
    return jsonify({"erro": "Usuário não encontrado."}), 404





if __name__ == "__main__":
    app.run(debug=True)
