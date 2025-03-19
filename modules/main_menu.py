from tkinter import *
import customtkinter as ctk
from PIL import Image

# Import specific functions from modules
from modules.add_book import add_book
from modules.remove_book import remove_book
from modules.add_loan import add_loan
from modules.end_loan import end_loan
from modules.show_students import show_students

def main_menu():
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
    title_label = ctk.CTkLabel(master=frame_menu, text="Bem-Vindo à Biblioteca!", font=("Roboto", 20, 'bold'), text_color="black", wraplength=230)  # Ajuste de wraplength se necessário
    title_label.pack(pady=40)

    buttons_data = [
        {"icon": ctk.CTkImage(light_image=Image.open("assets/loanbook.jpeg"), size=(20, 20)), "text": "Novo Empréstimo", "command": lambda: add_loan(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/returnbook.jpeg"), size=(20, 20)), "text": "Devolução de Livro", "command": lambda: end_loan(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/addbook.jpeg"), size=(20, 20)), "text": "Adicionar Livro", "command": lambda: add_book(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/removebook.jpeg"), size=(20, 20)), "text": "Remover Livro", "command": lambda: remove_book(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/alunos.jpeg"), size=(20, 20)), "text": "Lista de Alunos", "command": show_students},
    ]

    for button_data in buttons_data:
        frame_button = ctk.CTkFrame(master=frame_menu, fg_color="#FDFFEC", corner_radius=0)
        frame_button.pack(fill="x", pady=5)

        button = ctk.CTkButton(
            master=frame_button,
            text="      " + button_data["text"],  # Adiciona espaços em branco para simular o espaçamento
            font=("Roboto", 16),
            width=260,
            height=40,  # Ajuste a largura para acompanhar a sidebar
            fg_color="#FDFFEC",  # Cor do botão igual à do retângulo
            hover_color="#EEF0D8",  # Cor ao passar o mouse
            corner_radius=0,  # Deixar os botões sem cantos arredondados para uniformidade
            text_color="black",
            anchor="w",  # Alinha o texto à esquerda
            image=button_data["icon"],  # Adiciona o ícone ao botão
            compound="left", # Posiciona o ícone à esquerda do texto
            command=button_data["command"]
        )
        button.pack(fill="x", pady=0)  # Preenchimento horizontal e espaçamento menor entre os botões

    # Texto no final do menu
    credit_label = ctk.CTkLabel(
        master=frame_menu,
        text="Projeto dos Alunos do ITA para a\nEscola Estadual José Mariotto\nFerreira Aviador (SJC - SP)",
        font=("Roboto", 14),
        text_color="black"
    )
    credit_label.pack(pady=10, side="bottom")

    # Frame principal da tela
    main_frame = ctk.CTkFrame(master=root, fg_color="#F2F2F2")
    main_frame.pack(side="right", expand=True, fill="both")

    # Carrega a imagem principal (substitua 'caminho_para_imagem_principal.png' pelo caminho da imagem)
    imagem_principal = ctk.CTkImage(light_image=Image.open("assets/imagemFramePrincipal.jpeg"), size=(500, 500))
    label_imagem_principal = ctk.CTkLabel(master=main_frame, image=imagem_principal, text="")
    label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem

    # Texto no canto inferior direito
    quote_label = ctk.CTkLabel(
        master=main_frame,
        text="“A educação é a arma mais poderosa que você pode usar para mudar o mundo”\nNelson Mandela",
        font=("Roboto", 16, 'italic'),
        text_color="black",
        justify="left"
    )
    quote_label.pack(side="bottom", padx = 20, pady=20, anchor="se")

    # Inicializa a interface
    root.mainloop()
