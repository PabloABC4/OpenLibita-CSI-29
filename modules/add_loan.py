from tkinter import *
from tkinter import ttk, messagebox
import backend
from datetime import datetime

def add_loan(root):
    """
    Creates a new loan in the database.

    Collects book details from the user and submits them to the backend.
    Displays appropriate message boxes for errors and success.
    
    Args:
        root: The root window from which this function is called
    """
    def submit_loan():
        id_usuario = id_usuario_entry.get()
        id_livro = id_livro_entry.get()
        data_emprestimo = data_emprestimo_entry.get()
        data_prevista_devolucao = data_prevista_devolucao_entry.get()

        if not id_usuario or not id_livro or not data_emprestimo or not data_prevista_devolucao:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return
        
        try:
            # Ensure the dates are in the correct format
            data_emprestimo = datetime.strptime(data_emprestimo, '%d/%m/%Y').strftime('%Y-%m-%d')
            data_prevista_devolucao = datetime.strptime(data_prevista_devolucao, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Erro", "Datas inválidas. Use o formato DD/MM/AAAA.")
            return

        result = backend.add_loan(id_usuario, id_livro, data_emprestimo, data_prevista_devolucao)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", f"Empréstimo adicionado com sucesso. ID do Empréstimo: {result}")
            add_loan_window.destroy()

    add_loan_window = Toplevel(root)
    add_loan_window.title('Adicionar Empréstimo')
    add_loan_window.geometry("400x400")

    def create_label_entry(parent, text, row):
        ttk.Label(parent, text=text).grid(column=0, row=row, padx=10, pady=5)
        entry = ttk.Entry(parent)
        entry.grid(column=1, row=row, padx=10, pady=5)
        return entry
    
    id_usuario_entry = create_label_entry(add_loan_window, "ID do Aluno:", 0)
    id_livro_entry = create_label_entry(add_loan_window, "ID do Livro:", 1)
    data_emprestimo_entry = create_label_entry(add_loan_window, "Data do Empréstimo:", 2)
    data_prevista_devolucao_entry = create_label_entry(add_loan_window, "Data de Devolução:", 3)

    ttk.Button(add_loan_window, text="Enviar", command=submit_loan).grid(column=0, row=7, columnspan=2, pady=10)
