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

    page_index = 0
    students_per_page = 10

    tree = ttk.Treeview(new_root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150 if col != "email_usuario" else 200, anchor=CENTER)
    tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    previous_page_button = Button(new_root, text="Página Anterior", command=previous_page)
    previous_page_button.grid(row=1, column=0, pady=10)      

    next_page_button = Button(new_root, text="Próxima Página", command=next_page)    
    next_page_button.grid(row=1, column=1, pady=10)

    display_students()
