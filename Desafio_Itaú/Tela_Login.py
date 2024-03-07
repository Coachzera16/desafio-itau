import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='231203',
    database='desafio_itau',
)

cursor = conexao.cursor()

def login(usuario_entry, janela_login, senha_entry, janela_principal):
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    # Validação de campos vazios
    if usuario == "" or senha == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    # Validação de login (substitua por sua lógica de autenticação)
    if usuario == "admin" and senha == "1234":
        # Fechar a janela de login
        janela_login.destroy()

        # Criar a janela principal após a autenticação
        janela_principal.deiconify()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos.")

def mostrar_tela_login():
    # Criação da janela de login
    janela_login = Tk()
    janela_login.geometry("300x200")
    janela_login.title("Login")

    # Criação dos labels
    usuario_label = Label(janela_login, text="Usuário:")
    senha_label = Label(janela_login, text="Senha:")

    # Criação das entradas de texto
    usuario_entry = Entry(janela_login)
    senha_entry = Entry(janela_login, show="*")

    # Criação do botão
    botao_login = Button(janela_login, text="Login", command=lambda: login(usuario_entry, janela_login, senha_entry,janela), fg="white", bg="blue")

    # Posicionamento dos widgets
    usuario_label.place(x=10, y=10)
    usuario_entry.place(x=70, y=10)
    senha_label.place(x=10, y=40)
    senha_entry.place(x=70, y=40)
    botao_login.place(x=100, y=70)

    # Cor de fundo da janela
    janela_login.configure(bg="#f28500")

    # Execução da aplicação
    janela_login.mainloop()

def criar():
    nome = nome_entry.get()
    estado = estado_entry.get()
    tipo_conta = tipo_conta_var.get()

    # Validação de campo de nome vazio
    if nome == "":
        error_label.place(x=200, y=10)
        error_label.config(text="Erro: Preencha o campo Nome.")
        return
    else:
        # Limpar mensagem de erro se não houver erro
        error_label.config(text="")

    # Validação do tamanho do campo Estado
    if len(estado) > 2:
        error_label.place(x=200, y=40)
        error_label.config(text="Erro: máximo 2 caracteres.")
        return
    elif estado.isdigit():
        error_label.place(x=200, y=40)
        error_label.config(text="Erro: apenas letras são aceitas")
        return
    else:
        # Limpar mensagem de erro se não houver erro
        error_label.config(text="")

    comando = f'INSERT INTO cadastro (Nome, Estado, TipoConta) VALUES ("{nome}", "{estado}", "{tipo_conta}")'
    cursor.execute(comando)
    conexao.commit()
    mostrar_registros()

def ler():
    comando = f'SELECT * FROM cadastro'
    cursor.execute(comando)
    registros = cursor.fetchall()
    lista_registros.delete(0, END)
    for registro in registros:
        lista_registros.insert(END, f"{registro[0]} - {registro[1]} - {registro[2]} - {registro[3]}")

def atualizar():
    nome = nome_entry.get()
    estado = estado_entry.get()
    tipo_conta = tipo_conta_var.get()
    id = int(lista_registros.get(ANCHOR).split(" - ")[0])
    comando = f'UPDATE cadastro SET Nome = "{nome}", Estado = "{estado}", TipoConta = "{tipo_conta}" WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()
    mostrar_registros()

def deletar():
    id = int(lista_registros.get(ANCHOR).split(" - ")[0])
    comando = f'DELETE FROM cadastro WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()
    mostrar_registros()

def mostrar_registros():
    global cursor
    comando = f'SELECT * FROM cadastro'
    cursor.execute(comando)
    registros = cursor.fetchall()
    lista_registros.delete(0, END)
    for registro in registros:
        lista_registros.insert(END, f"{registro[0]} - {registro[1]} - {registro[2]} - {registro[3]}")





# Esconder a janela principal até o login ser bem-sucedido
janela = Tk()
label=Label(janela,text= "Autenticação Completa (Feche a janela para continuar)")
janela.withdraw()
label.pack()

# Mostrar a tela de login
mostrar_tela_login()

# Criação da janela principal
janela = Tk()
janela.geometry("500x300")

# Criação dos labels
nome_label = Label(janela, text="Nome:")
estado_label = Label(janela, text="Estado:")
tipo_conta_label = Label(janela, text="Tipo de Conta:")
error_label = Label(janela, text="", fg="red")

# Criação das entradas de texto
nome_entry = Entry(janela)
estado_entry = Entry(janela)

# Criação do menu de opções
tipo_conta_var = StringVar()
tipo_conta_var.set("Varejo")
tipo_conta_menu = OptionMenu(janela, tipo_conta_var, "Varejo", "Personalite", "PJ")

# Criação dos botões
botao_criar = Button(janela, text="Criar", command=criar, fg="white", bg="blue")
botao_ler = Button(janela, text="Ler", command=ler, fg="white", bg="blue")
botao_atualizar = Button(janela, text="Atualizar", command=atualizar, fg="white", bg="blue")
botao_deletar = Button(janela, text="Deletar", command=deletar, fg="white", bg="blue")

# Criação da lista de registros
lista_registros = Listbox(janela, height= 10,width= 50)

# Posicionamento dos widgets
nome_label.place(x=10, y=10)
nome_entry.place(x=70, y=10)
estado_label.place(x=10, y=40)
estado_entry.place(x=70, y=40)
tipo_conta_label.place(x=10, y=70)
tipo_conta_menu.place(x=100, y=70)
error_label.place(x=200, y=40)
botao_criar.place(x=10, y=100)
botao_ler.place(x=80, y=100)
botao_atualizar.place(x=150, y=100)
botao_deletar.place(x=220, y=100)
lista_registros.place(x=10, y=130)

# Cor de fundo da janela
janela.configure(bg="#f28500")

# Execução da aplicação
janela.mainloop()
