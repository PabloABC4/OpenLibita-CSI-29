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

    def edit_student(student_id):
        # Procurar o estudante pelo ID
        student_data = None
        for student in students:
            if student[0] == student_id:
                student_data = student
                break
        
        if not student_data:
            messagebox.showerror("Erro", "Estudante não encontrado.")
            return
        
        # Criar janela de edição
        edit_window = Toplevel()
        edit_window.title('Editar Aluno')
        edit_window.geometry("500x300")
        
        edit_window.grid_columnconfigure(0, weight=1)
        edit_window.grid_columnconfigure(1, weight=2)
        
        # Criar campos de formulário preenchidos com os dados atuais
        nome_label = create_label(edit_window, "Nome:", row=0, column=0, padx=10, pady=10, sticky=E)
        nome_entry = create_entry(edit_window, "", row=0, column=1, padx=10, pady=10, sticky=W)
        nome_entry.insert(0, student_data[1])
        
        email_label = create_label(edit_window, "Email:", row=1, column=0, padx=10, pady=10, sticky=E)
        email_entry = create_entry(edit_window, "", row=1, column=1, padx=10, pady=10, sticky=W)
        email_entry.insert(0, student_data[2])
        
        telefone_label = create_label(edit_window, "Telefone:", row=2, column=0, padx=10, pady=10, sticky=E)
        telefone_entry = create_entry(edit_window, "", row=2, column=1, padx=10, pady=10, sticky=W)
        telefone_entry.insert(0, student_data[3])
        
        # Função para salvar as alterações
        def save_changes():
            nome = nome_entry.get()
            email = email_entry.get()
            telefone = telefone_entry.get()
            
            if not nome:
                messagebox.showerror("Erro", "O nome do aluno é obrigatório.")
                return
            
            result = backend.update_student(student_id, nome, email, telefone)
            if isinstance(result, str):
                messagebox.showerror("Erro", result)
            else:
                messagebox.showinfo("Sucesso", "Informações do aluno atualizadas com sucesso.")
                edit_window.destroy()
                # Atualizar a lista de alunos
                show_students(main_frame)
        
        # Botão para salvar alterações
        save_button = create_button(edit_window, "Salvar Alterações", save_changes, row=3, column=0, columnspan=2, padx=20, pady=20)

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
    
    # Modificamos a forma como usamos a paginação para incluir botões de edição
    students_per_page = 5
    column_widths = [100, 200, 300, 150]  # Larguras para cada coluna
    
    # Criar uma instância personalizada do Pagination
    class EditablePagination(Pagination):
        def display(self):
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Adicionar cabeçalho de colunas
            for col_index, col in enumerate(self.columns):
                col_label = ctk.CTkLabel(master=self.scrollable_frame, text=col, font=("Roboto", 12, 'bold'))
                col_label.grid(row=0, column=col_index, padx=5, pady=2, sticky='ew')
                self.scrollable_frame.grid_columnconfigure(col_index, weight=1, minsize=self.column_widths[col_index])
            
            # Adicionar coluna de ações
            action_label = ctk.CTkLabel(master=self.scrollable_frame, text="Ações", font=("Roboto", 12, 'bold'))
            action_label.grid(row=0, column=len(self.columns), padx=5, pady=2, sticky='ew')
            self.scrollable_frame.grid_columnconfigure(len(self.columns), weight=1, minsize=100)

            # Mostrar dados da página atual
            current_page_data = self.data[self.items_per_page * self.current_index: self.items_per_page * (self.current_index + 1)]
            for i, item in enumerate(current_page_data):
                formatted_data = self.format(item)
                for j, value in enumerate(formatted_data):
                    value_label = ctk.CTkLabel(master=self.scrollable_frame, text=value)
                    value_label.grid(row=i + 1, column=j, padx=5, pady=2)
                
                # Adicionar botão de edição para cada linha
                edit_btn = create_button(
                    self.scrollable_frame, 
                    "Editar", 
                    lambda student_id=item[0]: edit_student(student_id),
                    row=i + 1, 
                    column=len(self.columns), 
                    padx=5, 
                    pady=2
                )

            # Atualizar estado dos botões de navegação
            self.previous_page_button.configure(state="normal" if self.current_index > 0 else "disabled")
            self.next_page_button.configure(state="normal" if self.items_per_page * (self.current_index + 1) < len(self.data) else "disabled")
    
    # Usar nossa classe personalizada de paginação
    students_pagination = EditablePagination(main_frame, students, columns, students_per_page, format_student, column_widths=column_widths)
    
    # Adicionar entrada para consulta de empréstimos de aluno
    student_id_label = create_label(main_frame, "ID do Aluno", row=3, column=0, padx=(80, 0), pady=(20, 5), sticky=E)
    student_id_entry = create_entry(main_frame, "Digite o ID do Aluno", row=3, column=1, padx=(80, 0), pady=(20, 5), sticky=W)
    
    # Botão para mostrar empréstimos
    create_button(main_frame, "Mostrar Empréstimos", show_student_loans, row=4, column=0, padx=(160, 160), pady=20, sticky=EW, columnspan=9)
