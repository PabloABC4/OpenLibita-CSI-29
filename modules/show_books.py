from tkinter import *
from tkinter import ttk, messagebox
import backend

def show_books():
    """
    Fetches and displays a list of books from the backend in a new window.

    If no books are found or an error occurs, appropriate message boxes are shown.
    """
    books, columns = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        return

    new_root = Toplevel()
    new_root.title('Lista de Livros')
    new_root.geometry("1050x400")

    tree = ttk.Treeview(new_root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=250 if col == "titulo" else 100, anchor=CENTER)  # Set width for each column
    tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    for book in books:
        formatted_book = (
            book[0],
            book[1],
            book[2],
            book[3],
            book[4],
            book[5],
            book[6],
            book[7]
        )
        tree.insert('', END, values=formatted_book)
