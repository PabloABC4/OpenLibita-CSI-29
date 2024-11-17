from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import backend
from datetime import datetime

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
        return

    if not loans:
        messagebox.showinfo("Info", "Nenhum empréstimo encontrado no banco de dados.")
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

    previous_page_button = ctk.CTkButton(main_frame, 
        text="Página Anterior", 
        font=("Roboto", 14, 'bold'),
        fg_color="#98a164",
        hover_color="#5c613e",
        text_color="#FFFFFF",
        corner_radius=2,
        border_width=1,
        border_color="#585c45",
        command=previous_page)
    previous_page_button.grid(row=1, column=0, padx=(80,10), pady=10, sticky="w")

    next_page_button =  ctk.CTkButton(main_frame, 
        text="Próxima Página", 
        font=("Roboto", 14, 'bold'),
        fg_color="#98a164",
        hover_color="#5c613e",
        text_color="#FFFFFF",
        corner_radius=2,
        border_width=1,
        border_color="#585c45",
        command=next_page)
    next_page_button.grid(row=1, column=1, padx=(10,80), pady=10, sticky="e")

    display_loans()

    ctk.CTkLabel(main_frame, text="ID do Empréstimo:", font=("Roboto", 14)).grid(row=2, column=0, padx=(80,0), pady=(20,5), sticky = 'w')
    loan_id_entry = ctk.CTkEntry(main_frame, placeholder_text="Digite o ID do Empréstimo", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    loan_id_entry.grid(row=2, column=1, pady=(20,5), sticky = 'w')

    ctk.CTkLabel(main_frame, text="Data Real de Devolução:", font=("Roboto", 14)).grid(row=3, column=0, padx=(80,0), pady=5, sticky = 'w')
    loan_end_date_entry = ctk.CTkEntry(main_frame, placeholder_text="Digite a Data da Devolução", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    loan_end_date_entry.grid(row=3, column=1, pady=5, sticky = 'w')

    ctk.CTkButton(main_frame, 
        text="Concluir Devolução", 
        font=("Roboto", 14, 'bold'),
        fg_color="#98a164",
        hover_color="#5c613e",
        text_color="#FFFFFF",
        corner_radius=2,
        border_width=1,
        border_color="#585c45",
        command=submit_ending
        ).grid(row=4, column=0, columnspan=2, padx =(160, 160), pady=20, sticky = "ew")
