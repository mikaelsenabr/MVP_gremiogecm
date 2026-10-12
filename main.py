from tkinter import *
from janela_principal import montar_janela_principal
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
janela_login.geometry("400x400")
janela_login.title("Login do Sistema")
janela_login.grab_set() # Torna a janela modal (foco total nela)

def verificar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "mikael" and senha == "1234":
        janela_login.destroy()       # Fecha a janela de login
        app_principal.deiconify()    # Revela a janela principal já carregada!
    else:
        label_confirmar.configure(text="Usuário ou Senha Inválido!!", text_color="red")

label_usuario = ctk.CTkLabel(janela_login, text="Usuário")
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(janela_login, placeholder_text="Digite o nome do usuário")
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(janela_login, text="Senha")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(janela_login, placeholder_text="Digite a senha", show="*")
campo_senha.pack(pady=10)

botao_entrar = ctk.CTkButton(janela_login, text="Entrar", command=verificar_login)
botao_entrar.pack(pady=10)

label_confirmar = ctk.CTkLabel(janela_login, text="")
label_confirmar.pack(pady=10)

app_principal.mainloop()