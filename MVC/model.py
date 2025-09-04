from config import db

class Tarefas(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pendente")
    id_usuario = db.Column(db.String(100),nullable=False)

    def __init__(self, titulo, descricao, status, id_usuario):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.id_usuario = id_usuario

    def transforma(self):
        return{
            'id': self.id,
            'nome': self.titulo,
            'descricao': self.descricao,
            'status': self.status,
            'id_usuario': self.id_usuario
        }
    
class TarefaNaoEncontrada(Exception):
    pass  

def criar_tarefa(dados):
    nova_tarefa = Tarefas(
        titulo = dados["titulo"],
        descricao = dados["descricao"],
        status = dados["status"],
        id_usuario = dados["id_status"]
    )

    db.session.add(nova_tarefa)
    db.session.commit()
    return {"mensagem" : "Tarefa criada com sucesso!"}, 201

def ler_tarefa():
    tarefas = Tarefas.query.all()
    print(tarefas)
    return [tarefa.transforma() for tarefa in tarefas]

def ler_tarefa_id(id_tarefa):
    tarefa = Tarefas.query.get(id_tarefa)
    if not tarefa:
        raise TarefaNaoEncontrada("Tarefa não encontrada!")
    return tarefa.transforma()

def atualizar_tarefa(id_tarefa, dados_novos):
    tarefa = Tarefas.query.get(id_tarefa)
    if not tarefa:
        raise TarefaNaoEncontrada("Tarefa não encontrada.")
    
    tarefa.titulo = dados_novos["titulo"]
    tarefa.descricao = dados_novos["descricao"]
    tarefa.status = dados_novos["status"]
    tarefa.id_usuario = dados_novos["id_usario"]

    db.session.commit()
    return {
        "id" : tarefa.id,
        "titulo" : tarefa.titulo,
        "descricao" : tarefa.descricao,
        "status" : tarefa.status,
        "id_usuario" : tarefa.id_usario
    }

def deletar_tarefa(id_tarefa):
    tarefa = Tarefas.query.get(id_tarefa)
    if not tarefa:
        raise TarefaNaoEncontrada("Tarefa não encontrada!")
    
    db.session.delete(tarefa)
    db.session.commit()