from model.usuario_model import Usuario, db

def criar_usuario(dados):
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    confirma_senha = dados.get('confirma_senha')

    if not nome or not email or not senha or confirma_senha is None:
        raise ValueError("Campos obrigatórios: nome, email, senha e confirma_senha.")
    
    if senha != confirma_senha:
        raise ValueError("As senhas não coincidem.")
    
    email_existente = Usuario.query.filter_by(email=email).first()
    if email_existente:
        raise ValueError("E-mail já cadastrado.")
    
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha=senha
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return novo_usuario

def listar_usuarios():
    return Usuario.query.all()

def listar_usuario_id(id):
    return Usuario.query.get(id)

def atualizar_usuario(id, dados):
    usuario = Usuario.query.get(id)
    if not usuario:
        raise ValueError("Usuário não encontrado.")
    
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    confirma_senha = ('confirma_senha')

    if nome:
        usuario.nome = nome

    if email and email != usuario.email:
        email_existente = Usuario.query.filter_by(email=email).first()
        if email_existente:
            raise ValueError("E-mail já está em uso por outro usuário.")
        usuario.email = email

    if senha:
        if not confirma_senha:
            raise ValueError("É necessário confirmar a nova senha.")
        if senha != confirma_senha:
            raise ValueError("As senhas não coincidem.")
        usuario.senha = senha

    db.session.commit()
    return usuario

def deletar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        raise ValueError("Usuário não encontrado.")

    db.session.delete(usuario)
    db.session.commit()
    return True

def autenticar_usuario(email, senha):
    return Usuario.query.filter_by(email=email, senha=senha).first()










