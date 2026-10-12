from database import conexao, cursor

def gerar_lista_membros():
    cursor.execute("""SELECT * FROM membros""")
    membros = cursor.fetchall() # Buscar todos os registros (como preencher a tabela com a lista completa de membros).

    return membros

def buscar_dados(id_deletar):
    cursor.execute("""SELECT nome, cargo, idade FROM membros WHERE id = ?""", (id_deletar,))
    membros = cursor.fetchall() # Buscar apenas um registro específico (como achar um usuário pelo ID na hora de atualizar)

    return membros

def cadastrar_no_banco(nome_digitado, cargo_digitado, idade_digitada):
    cursor.execute("""INSERT INTO membros (nome, cargo, idade) VALUES (?, ?, ?)""",(nome_digitado,cargo_digitado,idade_digitada))

    conexao.commit()

def atualizar_membro(coluna, dado_novo, id_digitado): # OK
    cursor.execute(f"UPDATE membros SET {coluna} = ? WHERE id = ?", (dado_novo, id_digitado))

    conexao.commit()

def deletar_membro(id_deletar): # OK
    cursor.execute("""DELETE FROM membros WHERE id = ?""",(id_deletar,))

    conexao.commit()
