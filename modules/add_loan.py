from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import backend
from datetime import datetime

def add_loan(frame_principal):
    """
    Modifica o frame_principal para exibir campos de digitação para um novo empréstimo.

    Args:
        frame_principal: O frame principal onde o conteúdo será exibido.
    """
    # Limpa o conteúdo atual do frame_principal
    for widget in frame_principal.winfo_children():
        widget.destroy()

    # Cria widgets de entrada e botões no frame_principal
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
        print(type(result))
        if isinstance(result, str):
            if result == "Indisponível":
                messagebox.showerror("Erro", "O livro solicitado está indisponível")
            else:
                messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Empréstimo adicionado com sucesso.")
            restaurar_frame_principal(frame_principal)  # Restaura o frame original após o envio

    # Cria função para restaurar o frame_principal com a imagem e citação
    def restaurar_frame_principal(frame_principal):
        for widget in frame_principal.winfo_children():
            widget.destroy()
        imagem_principal = ctk.CTkImage(light_image=Image.open("assets\\imagemFramePrincipal.jpeg"), size=(500, 500))
        label_imagem_principal = ctk.CTkLabel(master=frame_principal, image=imagem_principal, text="")
        label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")

        label_citacao = ctk.CTkLabel(
            master=frame_principal,
            text="“A educação é a arma mais poderosa que você pode usar para mudar o mundo”\nNelson Mandela",
            font=("Roboto", 16, 'italic'),
            text_color="black",
            justify="left"
        )
        label_citacao.pack(side="bottom", padx=20, pady=20, anchor="se")


    # Configuração dos campos de entrada com grid
    ctk.CTkLabel(frame_principal, text="ID do Livro:", font=("Roboto", 14)).grid(row=0, column=0, padx=(120,0), pady=(120,5), sticky="ew")
    id_livro_entry = ctk.CTkEntry(frame_principal, placeholder_text="Digite o ID do Livro", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    id_livro_entry.grid(row=1, column=0, padx=(120,0), pady=10, sticky = "ew")

    ctk.CTkLabel(frame_principal, text="ID do Aluno:", font=("Roboto", 14)).grid(row=0, column=2, padx=10, pady=(120,5), sticky="ew")
    id_usuario_entry = ctk.CTkEntry(frame_principal, placeholder_text="Digite o ID do Aluno", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    id_usuario_entry.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(frame_principal, text="Data do Empréstimo:", font=("Roboto", 14)).grid(row=2, column=0, padx=(120,0), pady=(10, 5), sticky="ew")
    data_emprestimo_entry = ctk.CTkEntry(frame_principal, placeholder_text="Digite a Data do Empréstimo", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    data_emprestimo_entry.grid(row=3, column=0, padx=(120,0), pady=(0, 10), sticky="ew")

    ctk.CTkLabel(frame_principal, text="Previsão de Devolução:", font=("Roboto", 14)).grid(row=2, column=2, padx=10, pady=10, sticky="ew")
    data_prevista_devolucao_entry = ctk.CTkEntry(frame_principal, placeholder_text="Digite a Previsão de Devolução", fg_color="#E0DFDF", corner_radius=2, border_color="#c2c0c0", border_width=1)
    data_prevista_devolucao_entry.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    # Botão centralizado na tela
    realizar_emprestimo_button = ctk.CTkButton(frame_principal,
                                            text="Realizar Empréstimo", 
                                            font=("Roboto", 14, 'bold'), 
                                            fg_color="#98a164",
                                            hover_color="#5c613e",
                                            text_color="#FFFFFF",
                                            corner_radius=2,
                                            border_width=1,
                                            border_color="#585c45",
                                            command=submit_loan)
    realizar_emprestimo_button.grid(row=4, column=0, columnspan=3, padx=(120,0) , pady=40, sticky ="ew")

    # Expande as colunas 1 e 3 para que os campos de entrada possam crescer horizontalmente
    frame_principal.grid_columnconfigure(1, weight=1)
    frame_principal.grid_columnconfigure(3, weight=1)
 