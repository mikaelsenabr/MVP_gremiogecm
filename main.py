from tkinter import *
from janela_principal import montar_janela_principal
from crud import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cria a janela principal do sistema, mas deixa ela oculta (.withdraw())
app_principal = ctk.CTk()
app_principal.withdraw()


# Monta todo o conteúdo do sistema na janela principal oculta
montar_janela_principal(app_principal)

# Cria a janela de Login como uma Toplevel acima da principal
janela_login = ctk.CTkToplevel(app_principal)
janela_login.geometry("400x430")
janela_login.title("Login do Sistema")
janela_login.grab_set() # Torna a janela modal (foco total nela)

tabela = ctk.CTkTabview(janela_login, width=350, height=500)
tabela.pack(pady=(20, 10))

tab_login = tabela.add("Login")
tab_registrar = tabela.add("Registrar-se")

# TABELA 1 - LOGIN

def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # TRAVA DE SEGURANÇA: Se algum campo estiver vazio, para aqui!
    if not usuario or not senha:
        label_confirmar_login.configure(text="Preencha todos os campos!", text_color="red")
        return

    resultado = verificar_usuario(usuario, senha)

    if resultado:
        janela_login.destroy()       # Fecha a janela de login
        app_principal.deiconify()    # Revela a janela principal já carregada!
    else:
        label_confirmar_login.configure(text="Usuário ou Senha Inválido. Registre-se!", text_color="red")


label_usuario = ctk.CTkLabel(tab_login, text="Usuário", font=("Helvetica", 18))
label_usuario.pack(pady=(20, 10))

campo_usuario = ctk.CTkEntry(tab_login, placeholder_text="Digite o nome do usuário", width=180)
campo_usuario.pack(pady=(20, 10))

label_senha = ctk.CTkLabel(tab_login, text="Senha", font=("Helvetica", 18))
label_senha.pack(pady=(20, 10))

campo_senha = ctk.CTkEntry(tab_login, placeholder_text="Digite a senha", show="*", width=180)
campo_senha.pack(pady=(20, 10))

botao_entrar = ctk.CTkButton(tab_login, text="Entrar", command=verificar_login)
botao_entrar.pack(pady=(20, 10))

label_confirmar_login = ctk.CTkLabel(tab_login, text="")
label_confirmar_login.pack(pady=(10, 0))

# TABELA 2 - REGISTRAR-SE
                                                                                                                                        
def registrar():
    usuario = campo_registrar_usuario.get()
    senha = campo_registrar_senha.get()
    confirmar_senha = campo_confirmar_senha.get()

    # TRAVA DE SEGURANÇA: Se algum campo estiver vazio, para aqui!
    if not usuario or not senha or not confirmar_senha:
        label_confirmar_registro.configure(text="Preencha todos os campos!", text_color="red")
        return

    if senha == confirmar_senha:
        resultado = verificar_usuario(usuario, confirmar_senha)
        
        if resultado is None:
                registrar_usuario(usuario, confirmar_senha)

                janela_login.destroy()       # Fecha a janela de login
                app_principal.deiconify()    # Revela a janela principal já carregada!
        else:
            label_confirmar_registro.configure(text="Usuário Já Cadastrado. Faça o Login!", text_color="red")

    else:
         label_confirmar_registro.configure(text="Senhas Diferentes. Digite Novamente!", text_color="red")


label_registrar_usuario = ctk.CTkLabel(tab_registrar, text="Usuário", font=("Helvetica", 16))
label_registrar_usuario.pack(pady=(10, 10))

campo_registrar_usuario = ctk.CTkEntry(tab_registrar, placeholder_text="Escolha o nome do usuário", width=180)
campo_registrar_usuario.pack(pady=(0, 10))

label_registrar_senha = ctk.CTkLabel(tab_registrar, text="Senha", font=("Helvetica", 16))
label_registrar_senha.pack(pady=(10, 10))

campo_registrar_senha = ctk.CTkEntry(tab_registrar, placeholder_text="Digite a senha desejada", show="*", width=180)
campo_registrar_senha.pack(pady=(0, 10))

label_confirmar_senha = ctk.CTkLabel(tab_registrar, text="Confirme a Senha", font=("Helvetica", 16))
label_confirmar_senha.pack(pady=(10, 10))

campo_confirmar_senha = ctk.CTkEntry(tab_registrar, placeholder_text="Confirme a Senha Desejada", show="*", width=180)
campo_confirmar_senha.pack(pady=(0, 10))

botao_registrar = ctk.CTkButton(tab_registrar, text="Registrar", command=registrar)
botao_registrar.pack(pady=(20, 10))

label_confirmar_registro = ctk.CTkLabel(tab_registrar, text="")
label_confirmar_registro.pack(pady=(10, 10))


app_principal.mainloop()