from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import modules.backend as backend
from modules.common import create_label, create_entry, create_button


def add_student(main_frame):
    """
    Opens a frame to add a new student to the database.

    Collects student details from the user and submits them to the backend.
    Displays appropriate message boxes for errors and success.
    
    Args:
        main_frame: The main frame where the student form will be displayed.
    """
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Configuração do grid para centralizar elementos
    main_frame.grid_columnconfigure(0, weight=1)  # Espaço à esquerda
    main_frame.grid_columnconfigure(1, weight=2)  # Coluna central para os campos
    main_frame.grid_columnconfigure(2, weight=1)  # Espaço à direita

    def submit_student():
        nome = nome_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()

        if not nome:
            messagebox.showerror("Erro", "O nome do aluno é obrigatório.")
            return

        student_id = backend.add_student(nome, email, telefone)
        if isinstance(student_id, str):
            messagebox.showerror("Erro", student_id)
        else:
            messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso. ID do aluno: " + str(student_id))
            restaurar_frame_principal(main_frame)

    # Cria função para restaurar o frame_principal com a imagem e citação
    def restaurar_frame_principal(main_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        imagem_principal = ctk.CTkImage(light_image=Image.open("assets/imagemFramePrincipal.jpeg"), size=(500, 500))
        label_imagem_principal = ctk.CTkLabel(master=main_frame, image=imagem_principal, text="")
        label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")

        label_citacao = ctk.CTkLabel(
            master=main_frame,
            text='"A educação é a arma mais poderosa que você pode usar para mudar o mundo"\nNelson Mandela',
            font=("Roboto", 16, 'italic'),
            text_color="black",
            justify="left"
        )
        label_citacao.pack(side="bottom", padx=20, pady=20, anchor="se")

    # Título
    titulo_label = ctk.CTkLabel(
        master=main_frame,
        text="Adicionar Novo Aluno",
        font=("Roboto", 24, 'bold'),
        text_color="black"
    )
    titulo_label.grid(row=0, column=1, pady=(50, 30), sticky="ew")

    # Campos de formulário centralizados na coluna 1
    nome_label = create_label(main_frame, "Nome do Aluno", row=1, column=1, pady=(10, 5), sticky="w")
    nome_entry = create_entry(main_frame, "Nome completo...", row=2, column=1, pady=5, sticky="ew")
    
    email_label = create_label(main_frame, "Email", row=3, column=1, pady=(15, 5), sticky="w")
    email_entry = create_entry(main_frame, "Email...", row=4, column=1, pady=5, sticky="ew")
    
    telefone_label = create_label(main_frame, "Telefone", row=5, column=1, pady=(15, 5), sticky="w")
    telefone_entry = create_entry(main_frame, "Telefone...", row=6, column=1, pady=5, sticky="ew")

    # Botão centralizado
    create_button(main_frame, "Adicionar Aluno", submit_student, row=7, column=1, pady=30, sticky="ew")
