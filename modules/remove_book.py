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
            if result == "Indisponível":
                messagebox.showerror("Erro", "Esse livro não pode ser removido pois está sendo emprestado.")
            else:
                messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Livro removido com sucesso.")
            remove_book_window.destroy()

    def display_books():
        current_page_books = books[books_per_page*page_index: books_per_page*(page_index+1)]
        for book in current_page_books:
            formatted_book = (
                book[0],
                book[1],
                book[2],
                book[3],
                book[4],
                "Sim" if book[5] else "Não", # Loan status
                book[7],
                book[8],
                book[9],
            )
            tree.insert('', END, values=formatted_book)
            
        if page_index == 0:
            previous_page_button.config(state=DISABLED)
        else:
            previous_page_button.config(state=NORMAL)

        if len(books) <= books_per_page*(page_index + 1):
            next_page_button.config(state=DISABLED)
        else:
            next_page_button.config(state=NORMAL)
    
    def next_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index += 1
        display_books()

    def previous_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index -= 1
        display_books()

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
    
    page_index = 0
    books_per_page = 10

    tree = ttk.Treeview(remove_book_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=250 if col == "titulo" else 100, anchor=CENTER)
    tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    

    previous_page_button = Button(remove_book_window, text="Página Anterior", command=previous_page)
    previous_page_button.grid(row=1, column=0, pady=10)      

    next_page_button = Button(remove_book_window, text="Próxima Página", command=next_page)    
    next_page_button.grid(row=1, column=1, pady=10)

    display_books()

    ttk.Label(remove_book_window, text="ID do Livro:").grid(column=0, row=2, padx=10, pady=5)
    book_id_entry = ttk.Entry(remove_book_window)
    book_id_entry.grid(column=1, row=2, padx=10, pady=5)

    delete_button = Button(remove_book_window, text="Enviar", command=submit_removal)
    delete_button.grid(row=3, column=0, columnspan=2, pady=10)