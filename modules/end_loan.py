from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from datetime import datetime
from modules.common import create_label, create_entry, create_button

def end_loan(main_frame):
    """
    Finishes a loan in the database.

    Fetches the list of loans from the backend and allows the user to input the ID of the loan to be removed.
    It also allows the user to input the return date.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called
    """
    for widget in main_frame.winfo_children():
        widget.destroy()

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
            restore_mainframe(main_frame)
    
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

    loans = backend.get_loans()
    if isinstance(loans, str):
        messagebox.showerror("Erro", loans)
        restore_mainframe(main_frame)
        return

    if not loans:
        messagebox.showinfo("Info", "Nenhum empréstimo encontrado no banco de dados.")
        restore_mainframe(main_frame)
        return

    page_index = 0
    loans_per_page = 7

    table_frame = ctk.CTkFrame(master=main_frame)
    table_frame.grid(row=0, column=0, columnspan=2, padx=80, pady=(120, 10), sticky="nsew")

    columns = ('ID Empréstimo', 'ID Usuário', 'ID Livro', 'Data Empréstimo', 'Data Prevista para Devolução')

    def display_loans():
        for widget in table_frame.winfo_children():
            widget.destroy()
        
        i = 0
        for col in columns:
            col_label = ctk.CTkLabel(master=table_frame, text=col, font=("Roboto", 12, 'bold'))
            col_label.grid(row = 0, column = i, padx = 5, pady = 2, sticky = 'w') 
            i = i + 1 

        current_page_loans = loans[loans_per_page * page_index: loans_per_page * (page_index + 1)]
        i = 1
        for loan in current_page_loans:
            j = 0
            formatted_loan = (
                loan[0],
                loan[1],
                loan[2],
                loan[3].strftime('%d/%m/%Y'),
                loan[4].strftime('%d/%m/%Y')
            )
            for value in formatted_loan:
                value_label = ctk.CTkLabel(master=table_frame, text=value)
                value_label.grid(row=i, column=j, padx=5, pady=2)
                j = j + 1
            i = i + 1
            
        previous_page_button.configure(state="normal" if page_index > 0 else "disabled")
        next_page_button.configure(state="normal" if loans_per_page * (page_index + 1) < len(loans) else "disabled")

    def next_page():
        nonlocal page_index
        page_index += 1
        display_loans()

    def previous_page():
        nonlocal page_index
        page_index -= 1
        display_loans()

    previous_page_button = create_button(main_frame, "Página Anterior", previous_page, row=1, column=0, padx=(100, 5), pady=10, sticky=W)
    next_page_button = create_button(main_frame, "Próxima Página", next_page, row=1, column=1, padx=(0, 100), pady=10, sticky=E)

    main_frame.grid_rowconfigure(2, minsize=50)  # Add this line to set the height of row 2

    display_loans()

    loan_id_label = create_label(main_frame, "ID do Empréstimo", row=3, column=0, padx=0, pady=5, sticky=EW)
    loan_id_entry = create_entry(main_frame, "ID do Empréstimo...", row=4, column=0, padx=100, pady=5, sticky=EW)
    
    loan_end_date_label = create_label(main_frame, "Data real de Devolução", row=3, column=1, padx=0, pady=5, sticky=EW)
    loan_end_date_entry = create_entry(main_frame, "Data real de Devolução...", row=4, column=1, padx=100, pady=5, sticky=EW)

    create_button(main_frame, "Concluir Devolução", submit_ending, row=5, column=0, columnspan=2, padx=(160, 160), pady=20)
