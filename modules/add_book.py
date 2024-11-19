from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from modules.common import create_label, create_entry, create_button


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

    title_label = create_label(main_frame, "Título", row=0, column=0, padx=(120, 0), pady=(120, 5), sticky=EW)
    title_entry = create_entry(main_frame, "Título...", row=1, column=0, padx=(120, 0), pady=10, sticky=EW)
    
    num_edicao_label = create_label(main_frame, "Número da Edição", row=0, column=2, padx=(0, 100), pady=(120, 5), sticky=EW)
    num_edicao_entry = create_entry(main_frame, "Número da Edição...", row=1, column=2, padx=(0, 100), pady=10, sticky=EW)
    
    num_exemplar_label = create_label(main_frame, "Número do Exemplar", row=2, column=0, padx=(120, 0), pady=(10, 5), sticky=EW)
    num_exemplar_entry = create_entry(main_frame, "Número do Exemplar...", row=3, column=0, padx=(120, 0), pady=10, sticky=EW)
    
    volume_label = create_label(main_frame, "Volume do Livro", row=2, column=2, padx=(0, 100), pady=(10, 5), sticky=EW)
    volume_entry = create_entry(main_frame, "Volume do Livro...", row=3, column=2, padx=(0, 100), pady=10, sticky=EW)
    
    id_editora_label = create_label(main_frame, "ID da Editora", row=4, column=0, padx=(120, 0), pady=(10, 5), sticky=EW)
    id_editora_entry = create_entry(main_frame, "ID da Editora...", row=5, column=0, padx=(120, 0), pady=10, sticky=EW)
    
    id_assunto_label = create_label(main_frame, "ID do Assunto", row=4, column=2, padx=(0, 100), pady=(10, 5), sticky=EW)
    id_assunto_entry = create_entry(main_frame, "ID do Assunto...", row=5, column=2, padx=(0, 100), pady=10, sticky=EW)
    
    id_localizacao_label = create_label(main_frame, "ID da Localização", row=6, column=1, pady=(10, 5), sticky=EW)
    id_localizacao_entry = create_entry(main_frame, "ID da Localização...", row=7, column=1, pady=10, sticky=EW)

    create_button(main_frame, "Adicionar Livro", submit_book, row=8, column=1, columnspan=1, padx=40, pady=10)
