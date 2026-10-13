from database import conexao, cursor

# CRUD DE MEMBROS
def cadastrar_membro(nome_digitado, cargo_digitado, idade_digitada):
    cursor.execute("""INSERT INTO membros (nome, cargo, idade) VALUES (?, ?, ?)""",(nome_digitado,cargo_digitado,idade_digitada))
    conexao.commit()

def atualizar_membro(coluna, dado_novo, id_digitado): # OK
    cursor.execute(f"UPDATE membros SET {coluna} = ? WHERE id = ?", (dado_novo, id_digitado))
    conexao.commit()

def deletar_membro(id_deletar): # OK
    cursor.execute("""DELETE FROM membros WHERE id = ?""",(id_deletar,))
    conexao.commit()

def buscar_dados_membros(id_deletar):
    cursor.execute("""SELECT nome, cargo, idade FROM membros WHERE id = ?""", (id_deletar,))
    membros = cursor.fetchone() # Buscar apenas um registro específico (como achar um usuário pelo ID na hora de atualizar)
    return membros

def gerar_lista_membros():
    cursor.execute("""SELECT * FROM membros""")
    membros = cursor.fetchall() # Buscar todos os registros (como preencher a tabela com a lista completa de membros).
    return membros


# CRUD DE AUTENTICAÇÃO
def registrar_usuario(usuario, senha):
    cursor.execute("""INSERT INTO usuarios (usuario, senha) VALUES (?, ?)""", (usuario, senha))
    conexao.commit()

def verificar_usuario(usuario, senha):
    cursor.execute("""SELECT * FROM usuarios WHERE usuario = ? AND senha = ?""", (usuario, senha))
    resultado = cursor.fetchone()

    return resultado
