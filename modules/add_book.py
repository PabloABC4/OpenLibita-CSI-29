from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from modules.common import LabelEntry


def add_book(main_frame):
    """
    Opens a new window to add a new book to the database.

    Collects book details from the user and submits them to the backend.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called.
    """
    for widget in main_frame.winfo_children():
        widget.destroy()

    def submit_book():
        title = title_entry.get()
        num_edicao = num_edicao_entry.get()
        num_exemplar = num_exemplar_entry.get()
        volume = volume_entry.get()
        id_editora = id_editora_entry.get()
        id_assunto = id_assunto_entry.get()
        id_localizacao = id_localizacao_entry.get()

        if not title or not num_edicao or not num_exemplar or not volume or not id_editora or not id_assunto or not id_localizacao:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        book_id = backend.add_book(title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao)
        if isinstance(book_id, str):
            messagebox.showerror("Erro", book_id)
        else:
            messagebox.showinfo("Sucesso", "Livro adicionado com sucesso. ID do livro: " + str(book_id))
            restaurar_frame_principal(main_frame)

        # Cria função para restaurar o frame_principal com a imagem e citação
    def restaurar_frame_principal(main_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        imagem_principal = ctk.CTkImage(light_image=Image.open("assets\\imagemFramePrincipal.jpeg"), size=(500, 500))
        label_imagem_principal = ctk.CTkLabel(master=main_frame, image=imagem_principal, text="")
        label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")

        label_citacao = ctk.CTkLabel(
            master=main_frame,
            text="“A educação é a arma mais poderosa que você pode usar para mudar o mundo”\nNelson Mandela",
            font=("Roboto", 16, 'italic'),
            text_color="black",
            justify="left"
        )
        label_citacao.pack(side="bottom", padx=20, pady=20, anchor="se")

    title_entry = LabelEntry(main_frame, "Título", 0, 0, (120, 0), (120, 5), (120, 0), (0, 10))
    num_edicao_entry = LabelEntry(main_frame, "Número da Edição", 0, 2, (0, 100), (120, 5), (0, 100), (0, 10))
    num_exemplar_entry = LabelEntry(main_frame, "Número do Exemplar", 2, 0, (120, 0), (10, 5), (120, 0), (0, 10))
    volume_entry = LabelEntry(main_frame, "Volume do Livro", 2, 2, (0, 100), (10, 5), (0, 100), (0, 10))
    id_editora_entry = LabelEntry(main_frame, "ID da Editora", 4, 0, (120, 0), (10, 5), (120, 0), (0, 10))
    id_assunto_entry = LabelEntry(main_frame, "ID do Assunto", 4, 2, (0, 100), (10, 5), (0, 100), (0, 10))
    id_localizacao_entry = LabelEntry(main_frame, "ID da Localização", 6, 1, 0, (10, 5), 0, 10)

    # Botão centralizado na tela
    realizar_emprestimo_button = ctk.CTkButton(main_frame,
        text="Adicionar Livro", 
        font=("Roboto", 14, 'bold'), 
        fg_color="#98a164",
        hover_color="#5c613e",
        text_color="#FFFFFF",
        corner_radius=2,
        border_width=1,
        border_color="#585c45",
        command=submit_book)
    realizar_emprestimo_button.grid(row=8, column=1, pady=40, sticky="ew")

    # Expande as colunas 1 e 3 para que os campos de entrada possam crescer horizontalmente
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=1)
    main_frame.grid_columnconfigure(3, weight=1)