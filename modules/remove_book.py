from tkinter import *
from tkinter import ttk, messagebox
import backend

def remove_book(root):
    """
    Displays a list of current books and allows the user to remove a selected book.
    """
    def submit_removal():
        book_id = book_id_entry.get()

        if not book_id:
            messagebox.showerror("Erro", "ID do livro é obrigatório.")
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
    
    books, columns = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        return

    remove_book_window = Toplevel(root)
    remove_book_window.title('Remover Livro')
    remove_book_window.geometry("1050x400")

    tree = ttk.Treeview(remove_book_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=250 if col == "titulo" else 100, anchor=CENTER)
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

    ttk.Label(remove_book_window, text="ID do Livro:").grid(column=0, row=1, padx=10, pady=5)
    book_id_entry = ttk.Entry(remove_book_window)
    book_id_entry.grid(column=1, row=1, padx=10, pady=5)

    delete_button = Button(remove_book_window, text="Enviar", command=submit_removal)
    delete_button.grid(row=2, column=0, columnspan=2, pady=10)