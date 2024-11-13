from tkinter import *
from tkinter import ttk, messagebox
import backend

def remove_book(root):
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