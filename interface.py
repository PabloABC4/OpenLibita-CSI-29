from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import time
import backend

# Import specific functions from modules
from modules.add_book import add_book
from modules.remove_book import remove_book
from modules.show_books import show_books

# Configurações iniciais
ctk.set_appearance_mode("light")

# Janela principal
root = ctk.CTk()
root.geometry("1020x650")
root.title("Sistema de Gerenciamento de Biblioteca")

# Frame lateral esquerdo (menu) com largura aumentada
frame_menu = ctk.CTkFrame(master=root, width=280, height=600, fg_color="#FDFFEC")  # Largura ajustada para 250
frame_menu.pack(side="left", fill="y")

# Título no topo do menu
label_titulo = ctk.CTkLabel(master=frame_menu, text="Bem-Vindo à Biblioteca!", font=("Roboto", 20, 'bold'), text_color="black", wraplength=230)  # Ajuste de wraplength se necessário
label_titulo.pack(pady=40)

icones = [
    ctk.CTkImage(light_image=Image.open("assets\\loanbook.jpg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("assets\\returnbook.jpg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("assets\\listbook.jpg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("assets\\addbook.jpg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("assets\\removebook.jpg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("assets\\alunos.jpg"), size=(20, 20))
]

# Botões do menu com espaçamento simulado por espaços em branco
botoes = ["Novo Empréstimo", "Devolução de Livro", "Todos os Livros", "Adicionar Livro", "Remover Livro", "Alunos"]
comandos = [None, None, show_books, lambda: add_book(root), lambda: remove_book(root), None]

for i in range(len(botoes)):
    botao_frame = ctk.CTkFrame(master=frame_menu, fg_color="#FDFFEC", corner_radius=0)
    botao_frame.pack(fill="x", pady=5)

    botao = ctk.CTkButton(
        master=botao_frame,
        text="      " + str(botoes[i]),  # Adiciona espaços em branco para simular o espaçamento
        font=("Roboto", 16),
        width=260,
        height=40,  # Ajuste a largura para acompanhar a sidebar
        fg_color="#FDFFEC",  # Cor do botão igual à do retângulo
        hover_color="#EEF0D8",  # Cor ao passar o mouse
        corner_radius=0,  # Deixar os botões sem cantos arredondados para uniformidade
        text_color="black",
        anchor="w",  # Alinha o texto à esquerda
        image=icones[i],  # Adiciona o ícone ao botão
        compound="left", # Posiciona o ícone à esquerda do texto
        command=comandos[i]

    )
    botao.pack(fill="x", pady=0)  # Preenchimento horizontal e espaçamento menor entre os botões

# Texto no final do menu
label_credito = ctk.CTkLabel(
    master=frame_menu,
    text="Projeto dos Alunos do ITA para a\nEscola Estadual José Mariotto\nFerreira Aviador (SJC - SP)",
    font=("Roboto", 14),
    text_color="black"
)
label_credito.pack(pady=10, side="bottom")

# Frame principal da tela
frame_principal = ctk.CTkFrame(master=root, fg_color="#F2F2F2")
frame_principal.pack(side="right", expand=True, fill="both")

# Carrega a imagem principal (substitua 'caminho_para_imagem_principal.png' pelo caminho da imagem)
imagem_principal = ctk.CTkImage(light_image=Image.open("assets\\imagemFramePrincipal.jpg"), size=(500, 500))
label_imagem_principal = ctk.CTkLabel(master=frame_principal, image=imagem_principal, text="")
label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem

# Texto no canto inferior direito
label_citacao = ctk.CTkLabel(
    master=frame_principal,
    text="“A educação é a arma mais poderosa que você pode usar para mudar o mundo”\nNelson Mandela",
    font=("Roboto", 16, 'italic'),
    text_color="black",
    justify="left"
)
label_citacao.pack(side="bottom", padx = 20, pady=20, anchor="se")

# Inicializa a interface
root.mainloop()
