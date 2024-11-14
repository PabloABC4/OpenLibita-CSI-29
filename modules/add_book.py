from tkinter import *
from tkinter import ttk, messagebox
import backend

def add_book(root):
    """
    Opens a new window to add a new book to the database.

    Collects book details from the user and submits them to the backend.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called.
    """
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
            add_book_window.destroy()

    add_book_window = Toplevel(root)
    add_book_window.title('Adicionar Livro')
    add_book_window.geometry("400x400")

    def create_label_entry(parent, text, row):
        ttk.Label(parent, text=text).grid(column=0, row=row, padx=10, pady=5)
        entry = ttk.Entry(parent)
        entry.grid(column=1, row=row, padx=10, pady=5)
        return entry

    title_entry = create_label_entry(add_book_window, "Título:", 0)
    num_edicao_entry = create_label_entry(add_book_window, "Número da Edição:", 1)
    num_exemplar_entry = create_label_entry(add_book_window, "Número do Exemplar:", 2)
    volume_entry = create_label_entry(add_book_window, "Volume:", 3)
    id_editora_entry = create_label_entry(add_book_window, "ID da Editora:", 4)
    id_assunto_entry = create_label_entry(add_book_window, "ID do Assunto:", 5)
    id_localizacao_entry = create_label_entry(add_book_window, "ID da Localização:", 6)

    ttk.Button(add_book_window, text="Enviar", command=submit_book).grid(column=0, row=7, columnspan=2, pady=10)