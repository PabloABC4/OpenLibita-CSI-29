from tkinter import *
import customtkinter as ctk
from PIL import Image

# Import specific functions from modules
from modules.add_book import add_book
from modules.remove_book import remove_book
from modules.add_loan import add_loan
from modules.end_loan import end_loan
from modules.show_students import show_students
from modules.add_student import add_student

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

    # Frame principal da tela
    main_frame = ctk.CTkFrame(master=root, fg_color="#F2F2F2")
    main_frame.pack(side="right", expand=True, fill="both")

    # Variável para armazenar a referência ao botão ativo
    active_button = None
    active_frame = None
    ACTIVE_COLOR = "#b8c286"  # Cor mais clara para o botão ativo
    NORMAL_COLOR = "#FDFFEC"  # Cor normal dos botões
    HOVER_COLOR = "#EEF0D8"   # Cor ao passar o mouse

    # Função para ativar um botão e desativar os outros
    def activate_button(frame, button, command):
        nonlocal active_button, active_frame
        
        # Restaura o estilo do botão ativo anterior
        if active_button and active_frame:
            active_frame.configure(fg_color=NORMAL_COLOR)
            active_button.configure(fg_color=NORMAL_COLOR, hover_color=HOVER_COLOR)
        
        # Define o novo botão ativo
        active_button = button
        active_frame = frame
        
        # Aplica o estilo ativo
        frame.configure(fg_color=ACTIVE_COLOR)
        button.configure(fg_color=ACTIVE_COLOR, hover_color=ACTIVE_COLOR)
        
        # Executa o comando associado ao botão
        command()

    buttons_data = [
        {"icon": ctk.CTkImage(light_image=Image.open("assets/loanbook.jpeg"), size=(20, 20)), "text": "Novo Empréstimo", "command": lambda: add_loan(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/returnbook.jpeg"), size=(20, 20)), "text": "Devolução de Livro", "command": lambda: end_loan(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/addbook.jpeg"), size=(20, 20)), "text": "Adicionar Livro", "command": lambda: add_book(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/removebook.jpeg"), size=(20, 20)), "text": "Remover Livro", "command": lambda: remove_book(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/alunos.jpeg"), size=(20, 20)), "text": "Lista de Alunos", "command": lambda: show_students(main_frame)},
        {"icon": ctk.CTkImage(light_image=Image.open("assets/alunos.jpeg"), size=(20, 20)), "text": "Adicionar Aluno", "command": lambda: add_student(main_frame)},
    ]

    button_list = []  # Lista para armazenar referências aos botões

    for index, button_data in enumerate(buttons_data):
        frame_button = ctk.CTkFrame(master=frame_menu, fg_color=NORMAL_COLOR, corner_radius=0)
        frame_button.pack(fill="x", pady=5)
        
        # Criar uma função de comando que ativa o botão e executa o comando original
        command_func = button_data["command"]
        
        button = ctk.CTkButton(
            master=frame_button,
            text="      " + button_data["text"],  # Adiciona espaços em branco para simular o espaçamento
            font=("Roboto", 16),
            width=260,
            height=40,  # Ajuste a largura para acompanhar a sidebar
            fg_color=NORMAL_COLOR,  # Cor do botão igual à do retângulo
            hover_color=HOVER_COLOR,  # Cor ao passar o mouse
            corner_radius=0,  # Deixar os botões sem cantos arredondados para uniformidade
            text_color="black",
            anchor="w",  # Alinha o texto à esquerda
            image=button_data["icon"],  # Adiciona o ícone ao botão
            compound="left", # Posiciona o ícone à esquerda do texto
            command=lambda f=frame_button, b=index, cmd=command_func: activate_button(f, button_list[b], cmd)
        )
        button.pack(fill="x", pady=0)  # Preenchimento horizontal e espaçamento menor entre os botões
        button_list.append(button)

    # Texto no final do menu
    credit_label = ctk.CTkLabel(
        master=frame_menu,
        text="Projeto dos Alunos do ITA para a\nEscola Estadual José Mariotto\nFerreira Aviador (SJC - SP)",
        font=("Roboto", 14),
        text_color="black"
    )
    credit_label.pack(pady=10, side="bottom")

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
