from tkinter import *
from tkinter import ttk, messagebox
from modules.common import create_button, create_label, create_entry, Pagination
import modules.backend as backend
import customtkinter as ctk
from PIL import Image

def format_student(student):
    return (
        student[0],
        student[1],
        student[2],
        student[3]
    )

def show_students(main_frame):
    """
    Fetches and displays a list of students from the backend in the main frame.

    If no students are found or an error occurs, appropriate message boxes are shown.
    
    Args:
        main_frame: The main frame where student list will be displayed
    """
    def restaurar_frame_principal(main_frame):
        for widget in main_frame.winfo_children():
            widget.destroy()
        imagem_principal = ctk.CTkImage(light_image=Image.open("assets/imagemFramePrincipal.jpeg"), size=(500, 500))
        label_imagem_principal = ctk.CTkLabel(master=main_frame, image=imagem_principal, text="")
        label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")

        label_citacao = ctk.CTkLabel(
            master=main_frame,
            text='"A educação é a arma mais poderosa que você pode usar para mudar o mundo"\nNelson Mandela',
            font=("Roboto", 16, 'italic'),
            text_color="black",
            justify="left"
        )
        label_citacao.pack(side="bottom", padx=20, pady=20, anchor="se")

    def show_student_loans():
        student_id = student_id_entry.get()
        if not student_id:
            messagebox.showerror("Erro", "ID do aluno é obrigatório.")
            return

        if student_id not in [str(student[0]) for student in students]:
            messagebox.showerror("Erro", "ID de Aluno não encontrado.")
            return

        loans = backend.get_student_loans(student_id)
        if isinstance(loans, str):
            messagebox.showerror("Erro", loans)
            return

        if not loans:
            messagebox.showinfo("Info", "Nenhum empréstimo encontrado para este aluno.")
            return

        # Aqui continuamos usando uma janela popup para empréstimos
        loans_window = Toplevel()
        loans_window.title('Empréstimos do Aluno')
        loans_window.geometry("900x400")

        columns = ('ID Empréstimo', 'ID Livro', 'Data Empréstimo', 'Data Prevista Devolução', 'Data Devolução', 'Finalizado')
        loan_tree = ttk.Treeview(loans_window, columns=columns, show='headings')
        for col in columns:
            loan_tree.heading(col, text=col)
            loan_tree.column(col, width=150, anchor=CENTER)
        loan_tree.pack(expand=True, fill=BOTH)

        for loan in loans:
            formatted_loan = (
                loan[0],
                loan[1],
                loan[2].strftime('%d/%m/%Y'),
                loan[3].strftime('%d/%m/%Y'),
                loan[4].strftime('%d/%m/%Y') if loan[4] else '',
                'Sim' if loan[5] else 'Não'
            )
            loan_tree.insert('', END, values=formatted_loan)

    # Limpa o frame principal
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    students, columns = backend.get_students()
    if isinstance(students, str):
        messagebox.showerror("Erro", students)
        return

    if not students:
        messagebox.showinfo("Info", "Nenhum aluno encontrado no banco de dados.")
        restaurar_frame_principal(main_frame)
        return
    
    # Usar o componente Pagination, assim como na página de remover livros
    students_per_page = 5
    column_widths = [100, 200, 300, 150]  # Larguras para cada coluna
    students_pagination = Pagination(main_frame, students, columns, students_per_page, format_student, column_widths=column_widths)
    
    # Adicionar entrada para consulta de empréstimos de aluno
    student_id_label = create_label(main_frame, "ID do Aluno", row=3, column=0, padx=(80, 0), pady=(20, 5), sticky=E)
    student_id_entry = create_entry(main_frame, "Digite o ID do Aluno", row=3, column=1, padx=(80, 0), pady=(20, 5), sticky=W)
    
    # Botão para mostrar empréstimos
    create_button(main_frame, "Mostrar Empréstimos", show_student_loans, row=4, column=0, padx=(160, 160), pady=20, sticky=EW, columnspan=9)
