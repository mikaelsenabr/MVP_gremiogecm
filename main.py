from tkinter import *
import customtkinter as ctk
import sqlite3

conexao = sqlite3.connect("gremio.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS membros (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL,
                idade INTEGER NOT NULL
                )""")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("500x550")
janela.title("Login do Sistema")

# FUNÇÃO PRO TABVIEW
def atualizar_lista_membros():
    if tabela.get() == "Membros Cadastrados":
        # Limpa todos os widgets antigos de dentro do frame rolável
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Busca os dados atualizados no banco
        cursor.execute("""SELECT * FROM membros""")
        membros = cursor.fetchall()

        linha = 0
        for membro in membros:
            id, nome, cargo, idade = membro
            
            ctk.CTkLabel(frame, text="{}".format(id)).grid(row=linha, column=0, pady=20, padx=20)
            ctk.CTkLabel(frame, text="{}".format(nome)).grid(row=linha, column=1, pady=20, padx=20)
            ctk.CTkLabel(frame, text="{}".format(cargo)).grid(row=linha, column=2, pady=20, padx=20)
            ctk.CTkLabel(frame, text="{}".format(idade)).grid(row=linha, column=3, pady=20, padx=20)

            linha += 1

# CRIAÇÃO DO TABVIEW

tabela = ctk.CTkTabview(janela, width=350, height=500, command=atualizar_lista_membros)
tabela.pack(pady=10)

# Criação de Tabelas

tab_1 = tabela.add("Cadastrar") 
tab_2 = tabela.add("Membros Cadastrados") 
tab_3 = tabela.add("Atualizar Membro")
tab_4 = tabela.add("Deletar Membro")


# TABELA 1 - CADASTRAR

def cadastrar_membro():
    nome_digitado = campo_nome.get()
    cargo_digitado = campo_cargo.get()
    idade_digitada = campo_idade.get()

    cursor.execute("""INSERT INTO membros 
                    (nome, cargo, idade) VALUES
                    (?, ?, ?)""",(nome_digitado,cargo_digitado,idade_digitada))
    conexao.commit()

    resultado_cadastro.configure(text="{} cadastrado(a) com sucesso!".format(nome_digitado.split()[0]), text_color="green")

    campo_nome.delete(0, "end")
    campo_cargo.delete(0, "end")
    campo_idade.delete(0, "end")

#titulo = ctk.CTkLabel(janela, text="Login do Grêmio", font=("Roboto", 24, "bold"))
#titulo.pack(pady=40)

label_nome = ctk.CTkLabel(tab_1, text="Nome:", font=("Arial", 20))
label_nome.pack(pady=10)

campo_nome = ctk.CTkEntry(tab_1, placeholder_text="Seu Nome", width=300, height=40)
campo_nome.pack(pady=10)

label_cargo = ctk.CTkLabel(tab_1, text="Cargo:", font=("Arial", 20))
label_cargo.pack(pady=10)

campo_cargo = ctk.CTkEntry(tab_1, placeholder_text="Seu Cargo", width=300, height=40)
campo_cargo.pack(pady=10)

label_idade = ctk.CTkLabel(tab_1, text="Idade:", font=("Arial", 20))
label_idade.pack(pady=10)

campo_idade = ctk.CTkEntry(tab_1, placeholder_text="Sua Idade", width=300, height=40)
campo_idade.pack(pady=10)

resultado_cadastro = ctk.CTkLabel(tab_1, text='', font=("Arial", 20)) # Local onde vai aparecer o texto após Cadastrar
resultado_cadastro.pack(pady=10)

botao = ctk.CTkButton(tab_1, text="Cadastrar", command=cadastrar_membro, width=300, height=50)
botao.pack(pady=10)

# TABELA 2 - MEMBROS CADASTRADOS
# Loop dos Dados


# Cabeçalho fixo

cabecalho = ctk.CTkFrame(tab_2)
cabecalho.pack(fill="x", padx=20, pady=(10, 0))

for x in range(1):
    ctk.CTkLabel(cabecalho, text="ID", font=("Arial", 15)).grid(row=2, column=1, padx=15)
    ctk.CTkLabel(cabecalho, text="Nome", font=("Arial", 15)).grid(row=2, column=2, padx=60)
    ctk.CTkLabel(cabecalho, text="Cargo", font=("Arial", 15)).grid(row=2, column=3, padx=50)
    ctk.CTkLabel(cabecalho, text="Idade", font=("Arial", 15)).grid(row=2, column=4, padx=0)

# Criando o Scrollable Frame
frame = ctk.CTkScrollableFrame(tab_2,
                               width=400,
                               height=500,
                               )
frame.pack(pady=40)


# TABELA 3 - ATUALIZAR MEMBRO

def entrada_opcao(choice): # Executa ao Selecionar no OptionMenu
    selecionado = selecionar_opcao.get().lower()

    if selecionado == "idade":
        campo_dado_novo.configure(placeholder_text="Escolha a nova {}".format(choice))
    else:
        campo_dado_novo.configure(placeholder_text="Escolha o novo {}".format(choice))
        


def dado_selecionado(): # Executa ao clicar no Botão
    selecionado = selecionar_opcao.get().lower()
    id_digitado = campo_atualizar_id.get()

    if selecionado == "nome":
        cursor.execute("""SELECT nome, cargo FROM membros WHERE id = ?""",(id_digitado,))
        nome_atual = cursor.fetchall()

        if not nome_atual:
            label_confirmar_atualizar.configure(text="Membro não encontrado!", text_color="red")

        else:
            for n in nome_atual:
                nome_velho, cargo = n
                label_confirmar_atualizar.configure(text="{} era o(a) {} do Grêmio".format(nome_velho, cargo))                

                nome_novo = campo_dado_novo.get()
                label_sucesso_atualizado.configure(text="Agora {} é o novo(a) {} do Grêmio".format(nome_novo.title(), cargo.title(), text_color="green"))

                cursor.execute("""UPDATE membros SET nome = ? WHERE id = ?""",(nome_novo, id_digitado))
                conexao.commit()

    elif selecionado == "cargo":
        cursor.execute("""SELECT nome, cargo FROM membros WHERE id = ?""",(id_digitado,))
        cargo_atual = cursor.fetchall()

        if not cargo_atual:
            label_confirmar_atualizar.configure(text="Membro não encontrado!", text_color="red")

        else:
            for c in cargo_atual:
                nome, cargo_velho = c
                label_confirmar_atualizar.configure(text="{} era o(a) {} do Grêmio".format(nome, cargo_velho))

                cargo_novo = campo_dado_novo.get()
                label_sucesso_atualizado.configure(text="Agora {} é o novo(a) {} do Grêmio".format(nome.title(), cargo_novo.title()))

                cursor.execute("""UPDATE membros SET cargo = ? WHERE id = ?""",(cargo_novo, id_digitado))
                conexao.commit()

    elif selecionado == "idade":
        cursor.execute("""SELECT nome, cargo, idade FROM membros WHERE id = ?""",(id_digitado,))
        idade_atual = cursor.fetchall()

        if not idade_atual:
            label_confirmar_atualizar.configure(text="Membro não encontrado!", text_color="red")
        else:
            for d in idade_atual:
                nome, cargo, idade_velha = d
                label_confirmar_atualizar.configure(text="{} é o(a) {} do Grêmio e tinha {} anos".format(nome.title(), cargo.title(), idade_velha))

                idade_nova = campo_dado_novo.get()
                label_sucesso_atualizado.configure(text="Agora {}, tem {} anos atualmente".format(nome.title(), idade_nova))

                cursor.execute("""UPDATE membros SET idade = ? WHERE id = ?""",(idade_nova, id_digitado))
                conexao.commit()


label_atualizar_id = ctk.CTkLabel(tab_3, text="Digite o ID", font=("Arial", 20))
label_atualizar_id.pack(pady=10)

campo_atualizar_id = ctk.CTkEntry(tab_3, placeholder_text="ID", width=150, height=40)
campo_atualizar_id.pack(pady=10)

# Definindo as Opções do OptionMenu

opcoes = ["Nome", "Cargo", "Idade"]

# Criando OptionMenu

selecionar_opcao = ctk. CTkOptionMenu(tab_3, values=opcoes, command=entrada_opcao)
selecionar_opcao.pack(pady=10)

#Entrada Nova

campo_dado_novo = ctk.CTkEntry(tab_3, placeholder_text="", width=200)
campo_dado_novo.pack(pady=10)

#Botão Atualizar

botao_atualizar = ctk.CTkButton(tab_3, text="Atualizar", command=dado_selecionado)
botao_atualizar.pack(pady=10)

# Confirmação

label_confirmar_atualizar = ctk.CTkLabel(tab_3, text="")
label_confirmar_atualizar.pack(pady=10)

# Sucesso

label_sucesso_atualizado = ctk.CTkLabel(tab_3, text="")
label_sucesso_atualizado.pack(pady=10)


# TABELA 4 - DELETAR MEMBRO

# Buscar dados para confirmação
def buscar(choice):
    id_deletar = campo_deletar_id.get().lower()

    cursor.execute("""SELECT nome, cargo FROM membros WHERE id = ?""",(id_deletar,))
    dados = cursor.fetchall()

    if not dados:
        label_confirmar_deletar.configure(text="Membro não encontrado!", text_color="red")

    else:
        for d in dados:
            nome, cargo = d
            label_confirmar_deletar.configure(text="Deseja deletar {}, {} do Grêmio porque {}?".format(nome, cargo, choice), text_color="white")
            label_sucesso_deletado.configure(text="")

def deletar():
    id_deletar = campo_deletar_id.get()

    cursor.execute("""SELECT nome, cargo FROM membros WHERE id = ?""",(id_deletar,))
    dados = cursor.fetchall()

    if not dados:
        label_sucesso_deletado.configure(text="Por favor, mude o ID!", text_color="red")

    else:
        cursor.execute("""DELETE FROM membros WHERE id = ?""",(id_deletar,))
        label_sucesso_deletado.configure(text="Deletado com sucesso!", text_color="green")
        conexao.commit()



label_deletar_id = ctk.CTkLabel(tab_4, text="Digite o ID", font=("Arial", 20))
label_deletar_id.pack(pady=10)

campo_deletar_id = ctk.CTkEntry(tab_4, placeholder_text="ID", width=150, height=40,)
campo_deletar_id.pack(pady=10)

# Definindo as Opções do OptionMenu

motivo = ["Saiu", "Mudou de Cidade", "Faleceu"]

# Criando OptionMenu

selecionar_motivo = ctk. CTkOptionMenu(tab_4, values=motivo, command=buscar)
selecionar_motivo.pack(pady=10)

# Confirmação

label_confirmar_deletar = ctk.CTkLabel(tab_4, text="")
label_confirmar_deletar.pack(pady=10)

# Botão Deletar

botao_deletar = ctk.CTkButton(tab_4, text="Deletar", command=deletar)
botao_deletar.pack(pady=10)

label_sucesso_deletado = ctk. CTkLabel(tab_4, text="")
label_sucesso_deletado.pack(pady=10)


janela.mainloop()