from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import backend

def show_books():
    books = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        return

    new_root = Toplevel()
    new_root.title('Lista de Livros')
    new_root.geometry("400x300")
    new_frm = ttk.Frame(new_root, padding=10)
    new_frm.grid(sticky=(N, S, E, W))

    new_root.columnconfigure(0, weight=1)
    new_root.rowconfigure(0, weight=1)
    new_frm.columnconfigure(0, weight=1)

    for idx, book in enumerate(books):
        text = f"{idx + 1}. {book}"
        ttk.Label(new_frm, text=text).grid(column=0, row=idx)

def add_book():
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

        result = backend.add_book(title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Livro adicionado com sucesso.")
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

def remove_book():
    def submit_removal():
        book_id = book_id_entry.get()

        if not book_id:
            messagebox.showerror("Erro", "ID do Livro é obrigatório.")
            return

        if book_id not in [str(book[0]) for book in books]:
            messagebox.showerror("Erro", "ID de Livro não encontrado.")
            return

        result = backend.remove_book(book_id)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Livro removido com sucesso.")
            remove_book_window.destroy()

    books = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        return

    remove_book_window = Toplevel(root)
    remove_book_window.title('Remover Livro')
    remove_book_window.geometry("300x200")

    ttk.Label(remove_book_window, text="ID do Livro:").grid(column=0, row=0, padx=10, pady=5)
    book_id_entry = ttk.Entry(remove_book_window)
    book_id_entry.grid(column=1, row=0, padx=10, pady=5)

    ttk.Button(remove_book_window, text="Enviar", command=submit_removal).grid(column=0, row=1, columnspan=2, pady=10)

    ttk.Button(remove_book_window, text="Sair", command=remove_book_window.destroy).grid(column=1, row=2, columnspan=2, padx=10, pady=10, stick=S)


root = Tk()
root.title('Sistema de Gerenciamento de Biblioteca')
root.geometry("564x480")
frm = ttk.Frame(root, padding=10)
frm.pack(side=TOP)

ttk.Label(frm, text="Bem-vindo ao OpenLibITA", font=15).pack(pady=10)
ttk.Button(frm, text="Adicionar Livro", command=add_book).pack(pady=10)
ttk.Button(frm, text="Mostrar Livros", command=show_books).pack(pady=10)
ttk.Button(frm, text="Remover Livro", command=remove_book).pack(pady=10)

ttk.Button(frm, text="Sair", command=root.destroy).pack(pady=10)
root.mainloop()
