from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from datetime import datetime
from modules.common import create_label, create_entry, create_button, Pagination

def end_loan(master):
    """
    Finishes a loan in the database.

    Fetches the list of loans from the backend and allows the user to input the ID of the loan to be removed.
    It also allows the user to input the return date.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called
    """
    def format_loan(loan):
        return (
            loan[0],
            loan[1],
            loan[2],
            loan[3].strftime('%d/%m/%Y'),
            loan[4].strftime('%d/%m/%Y')
        )
    
    def submit_ending():
        loan_id = loan_id_entry.get()
        loan_end_date = loan_end_date_entry.get()

        if not loan_id or not loan_end_date:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        try:
            # Ensure the date is in the correct format
            loan_end_date = datetime.strptime(loan_end_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Erro", "Data de devolução inválida. Use o formato DD/MM/AAAA.")
            return

        if loan_id not in [str(loan[0]) for loan in loans]:
            messagebox.showerror("Erro", "ID de Empréstimo não encontrado.")
            return
        
        result = backend.end_loan(loan_id, loan_end_date)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Empréstimo concluído com sucesso.")
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

    loans, columns = backend.get_loans()
    if isinstance(loans, str):
        messagebox.showerror("Erro", loans)
        restore_mainframe(master)
        return

    if not loans:
        messagebox.showinfo("Info", "Nenhum empréstimo encontrado no banco de dados.")
        restore_mainframe(master)
        return

    master.grid_rowconfigure(2, minsize=50)  # Add this line to set the height of row 2

    loans_per_page = 5
    Pagination(master, loans, columns, loans_per_page, format_loan)

    loan_id_label = create_label(master, "ID do Empréstimo", row=3, column=0, padx=0, pady=5, sticky=EW)
    loan_id_entry = create_entry(master, "ID do Empréstimo...", row=4, column=0, padx=100, pady=5, sticky=EW)
    
    loan_end_date_label = create_label(master, "Data real de Devolução", row=3, column=len(columns)-2, columnspan=2, padx=(0, 20), pady=5, sticky=EW)
    loan_end_date_entry = create_entry(master, "Data real de Devolução...", row=4, column=len(columns)-2, columnspan=2, padx=(0, 30), pady=5, sticky=EW)

    create_button(master, "Concluir Devolução", submit_ending, row=5, column=0, columnspan=2, padx=(160, 160), pady=20)
