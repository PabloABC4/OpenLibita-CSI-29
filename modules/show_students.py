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

    tree = ttk.Treeview(new_root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150 if col != "email_usuario" else 200, anchor=CENTER)
    tree.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    for student in students:
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
