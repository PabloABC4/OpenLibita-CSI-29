from tkinter import *
from tkinter import ttk, messagebox
import backend

def show_students():
    """
    Fetches and displays a list of students from the backend in a new window.

    If no students are found or an error occurs, appropriate message boxes are shown.
    """
    students, columns = backend.get_students()
    if isinstance(students, str):
        messagebox.showerror("Erro", students)
        return

    if not students:
        messagebox.showinfo("Info", "Nenhum aluno encontrado no banco de dados.")
        return

    new_root = Toplevel()
    new_root.title('Lista de Alunos')
    new_root.geometry("1300x400")

    def display_students():
        current_page_students = students[students_per_page*page_index: students_per_page*(page_index+1)]
        for student in current_page_students:
            formatted_student = (
                student[0],
                student[1],
                student[2],
                student[3],
                student[4],
                student[5],
                student[6],
                student[7]
            )
            tree.insert('', END, values=formatted_student)
            
        if page_index == 0:
            previous_page_button.config(state=DISABLED)
        else:
            previous_page_button.config(state=NORMAL)

        if len(students) <= students_per_page*(page_index + 1):
            next_page_button.config(state=DISABLED)
        else:
            next_page_button.config(state=NORMAL)
    
    def next_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index += 1
        display_students()

    def previous_page():
        for item in tree.get_children():
            tree.delete(item)
        nonlocal page_index
        page_index -= 1
        display_students()

    def show_student_loans():
        student_id = student_id_entry.get()
        if not student_id:
            messagebox.showerror("Erro", "ID do aluno é obrigatório.")
            return

        loans = backend.get_student_loans(student_id)
        if isinstance(loans, str):
            messagebox.showerror("Erro", loans)
            return

        if not loans:
            messagebox.showinfo("Info", "Nenhum empréstimo encontrado para este aluno.")
            return

        loans_window = Toplevel()
        loans_window.title('Empréstimos do Aluno')
        loans_window.geometry("900x400")

        columns = ('ID Empréstimo', 'ID Livro', 'Data Empréstimo', 'Data Prevista Devolução', 'Data Devolução', 'Finalizado')
        tree = ttk.Treeview(loans_window, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150, anchor=CENTER)
        tree.pack(expand=True, fill=BOTH)

        for loan in loans:
            formatted_loan = (
                loan[0],
                loan[1],
                loan[2].strftime('%d/%m/%Y'),
                loan[3].strftime('%d/%m/%Y'),
                loan[4].strftime('%d/%m/%Y') if loan[4] else '',
                'Sim' if loan[5] else 'Não'
            )
            tree.insert('', END, values=formatted_loan)

    page_index = 0
    students_per_page = 10

    tree = ttk.Treeview(new_root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150 if col != "email_usuario" else 200, anchor=CENTER)
    tree.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    previous_page_button = Button(new_root, text="Página Anterior", command=previous_page)
    previous_page_button.grid(row=1, column=0, pady=10, padx=(10, 5))      

    next_page_button = Button(new_root, text="Próxima Página", command=next_page)    
    next_page_button.grid(row=1, column=2, pady=10, padx=(5, 10))

    student_id_label = Label(new_root, text="Digite abaixo o ID de um aluno para ver seus empréstimos")
    student_id_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=N)

    student_id_label = Label(new_root, text="ID do Aluno:")
    student_id_label.grid(row=3, column=0, padx=10, pady=5, sticky=E)

    student_id_entry = Entry(new_root)
    student_id_entry.grid(row=3, column=1, padx=5, pady=5, stick=W)

    show_loans_button = Button(new_root, text="Mostrar Empréstimos", command=show_student_loans)
    show_loans_button.grid(row=3, column=2, pady=5, sticky=W)

    # Configure column widths
    new_root.grid_columnconfigure(0, weight=5)
    new_root.grid_columnconfigure(1, weight=1)
    new_root.grid_columnconfigure(2, weight=5)

    display_students()
