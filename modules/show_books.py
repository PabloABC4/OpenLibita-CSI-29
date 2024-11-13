from tkinter import *
from tkinter import ttk, messagebox
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