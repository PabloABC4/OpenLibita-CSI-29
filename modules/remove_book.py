from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from modules.common import create_button, create_entry, create_label, Pagination

def format_book(book):
    return (
        book[0],
        book[1],
        book[2],
        "Sim" if book[3] else "Não"
    )

def remove_book(master):
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
            restore_mainframe(master)

    def restore_mainframe(main_frame):
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

    books, columns = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        restore_mainframe(master)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        restore_mainframe(master)
        return
        
    books_per_page = 5
    column_widths = [100, 300, 200, 100]  # Example widths for each column
    remove_book_pagination = Pagination(master, books, columns, books_per_page, format_book, column_widths=column_widths)

    book_id_label = create_label(master, "ID do Livro", row=3, column=0, padx=(80, 0), pady=(20, 5), sticky=E)
    book_id_entry = create_entry(master, "Digite o ID do Livro", row=3, column=1, padx=(80, 0), pady=(20, 5), sticky=W)

    create_button(master, "Concluir Remoção", submit_removal, row=4, column=0, padx=(160, 160), pady=20, sticky=EW, columnspan=9)
