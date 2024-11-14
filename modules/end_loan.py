from tkinter import *
from tkinter import ttk, messagebox
import backend

def end_loan(root):
    """
    Finishes a loan in the database.

    Fetches the list of loans from the backend and allows the user to input the ID of the loan to be removed.
    It also allows the user to input the return date.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called
    """
    def submit_ending():
        loan_id = loan_id_entry.get()
        loan_end_date = loan_end_date_entry.get()

        if not loan_id or not loan_end_date:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        if loan_id not in [str(loan[0]) for loan in loans]:
            messagebox.showerror("Erro", "ID de Empréstimo não encontrado.")
            return
        
        result = backend.end_loan(loan_id, loan_end_date)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Empréstimo concluído com sucesso.")
            end_loan_window.destroy()

    def display_loans():
        current_page_loans = loans[loans_per_page * page_index: loans_per_page * (page_index + 1)]
        for loan in current_page_loans:
            formatted_loan = (
                loan[0],
                loan[1],
                loan[2],
                loan[3].strftime('%d/%m/%Y'),
                loan[4].strftime('%d/%m/%Y')
            )
            tree.insert('', END, values=formatted_loan)
            
        if page_index == 0:
            previous_page_button.config(state=DISABLED)
        else:
            previous_page_button.config(state=NORMAL)

        if len(loans) <= loans_per_page * (page_index + 1):
            next_page_button.config(state=DISABLED)
        else:
            next_page_button.config(state=NORMAL)

    def next_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index += 1
        display_loans()

    def previous_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index -= 1
        display_loans()

    loans = backend.get_loans()
    if isinstance(loans, str):
        messagebox.showerror("Erro", loans)
        return

    if not loans:
        messagebox.showinfo("Info", "Nenhum empréstimo encontrado no banco de dados.")
        return

    end_loan_window = Toplevel(root)
    end_loan_window.title('Devolução de Livro')
    end_loan_window.geometry("600x400")

    page_index = 0
    loans_per_page = 10

    columns = ('ID Empréstimo', 'ID Usuário', 'ID Livro', 'Data Empréstimo', 'Data Prevista para Devolução')
    tree = ttk.Treeview(end_loan_window, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
    tree.column('ID Empréstimo', width=90, anchor=CENTER)
    tree.column('ID Usuário', width=70, anchor=CENTER)
    tree.column('ID Livro', width=70, anchor=CENTER)
    tree.column('Data Empréstimo', width=120, anchor=CENTER)
    tree.column('Data Prevista para Devolução', width=170, anchor=CENTER)
    tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    previous_page_button = Button(end_loan_window, text="Página Anterior", command=previous_page)
    previous_page_button.grid(row=1, column=0, pady=10)

    next_page_button = Button(end_loan_window, text="Próxima Página", command=next_page)
    next_page_button.grid(row=1, column=1, pady=10)

    display_loans()

    ttk.Label(end_loan_window, text="ID do Empréstimo:").grid(column=0, row=2, padx=10, pady=5)
    loan_id_entry = ttk.Entry(end_loan_window)
    loan_id_entry.grid(column=1, row=2, padx=10, pady=5)

    ttk.Label(end_loan_window, text="Data Real de Devolução:").grid(column=0, row=3, padx=10, pady=5)
    loan_end_date_entry = ttk.Entry(end_loan_window)
    loan_end_date_entry.grid(column=1, row=3, padx=10, pady=5)

    ttk.Button(end_loan_window, text="Enviar", command=submit_ending).grid(column=0, row=4, columnspan=2, pady=10)
