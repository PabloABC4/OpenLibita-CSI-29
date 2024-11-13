from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import time
import backend

def show_books():
    books = backend.get_books()
    if isinstance(books, str):
        messagebox.showerror("Erro", books)
        return

    if not books:
        messagebox.showinfo("Info", "Nenhum livro encontrado no banco de dados.")
        return

    new_root = Toplevel()
    new_root.title('Lista de Livros')
    new_root.geometry("400x300")
    new_frm = ttk.Frame(new_root, padding=10)
    new_frm.grid(sticky=(N, S, E, W))

    new_root.columnconfigure(0, weight=1)
    new_root.rowconfigure(0, weight=1)
    new_frm.columnconfigure(0, weight=1)

    for idx, book in enumerate(books):
        text = f"{idx + 1}. {book}"
        ttk.Label(new_frm, text=text).grid(column=0, row=idx)

def add_book():
    def submit_book():
        title = title_entry.get()
        num_edicao = num_edicao_entry.get()
        num_exemplar = num_exemplar_entry.get()
        volume = volume_entry.get()
        id_editora = id_editora_entry.get()
        id_assunto = id_assunto_entry.get()
        id_localizacao = id_localizacao_entry.get()

        if not title or not num_edicao or not num_exemplar or not volume or not id_editora or not id_assunto or not id_localizacao:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        result = backend.add_book(title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Livro adicionado com sucesso.")
            add_book_window.destroy()

    add_book_window = Toplevel(root)
    add_book_window.title('Adicionar Livro')
    add_book_window.geometry("400x400")

    def create_label_entry(parent, text, row):
        ttk.Label(parent, text=text).grid(column=0, row=row, padx=10, pady=5)
        entry = ttk.Entry(parent)
        entry.grid(column=1, row=row, padx=10, pady=5)
        return entry

    title_entry = create_label_entry(add_book_window, "Título:", 0)
    num_edicao_entry = create_label_entry(add_book_window, "Número da Edição:", 1)
    num_exemplar_entry = create_label_entry(add_book_window, "Número do Exemplar:", 2)
    volume_entry = create_label_entry(add_book_window, "Volume:", 3)
    id_editora_entry = create_label_entry(add_book_window, "ID da Editora:", 4)
    id_assunto_entry = create_label_entry(add_book_window, "ID do Assunto:", 5)
    id_localizacao_entry = create_label_entry(add_book_window, "ID da Localização:", 6)

    ttk.Button(add_book_window, text="Enviar", command=submit_book).grid(column=0, row=7, columnspan=2, pady=10)

def remove_book():
    def submit_removal():
        book_id = book_id_entry.get()

        if not book_id:
            messagebox.showerror("Erro", "ID do Livro é obrigatório.")
            return

        result = backend.remove_book(book_id)
        if isinstance(result, str):
            messagebox.showerror("Erro", result)
        else:
            messagebox.showinfo("Sucesso", "Livro removido com sucesso.")
            remove_book_window.destroy()

    remove_book_window = Toplevel(root)
    remove_book_window.title('Remover Livro')
    remove_book_window.geometry("300x200")

    ttk.Label(remove_book_window, text="ID do Livro:").grid(column=0, row=0, padx=10, pady=5)
    book_id_entry = ttk.Entry(remove_book_window)
    book_id_entry.grid(column=1, row=0, padx=10, pady=5)

    ttk.Button(remove_book_window, text="Enviar", command=submit_removal).grid(column=0, row=1, columnspan=2, pady=10)


# Configurações iniciais
ctk.set_appearance_mode("light")

# Janela principal
root = ctk.CTk()
root.geometry("1020x650")
root.title("Sistema de Gerenciamento de Biblioteca")

# Frame lateral esquerdo (menu) com largura aumentada
frame_menu = ctk.CTkFrame(master=root, width=280, height=600, fg_color="#FDFFEC")  # Largura ajustada para 250
frame_menu.pack(side="left", fill="y")

# Título no topo do menu
label_titulo = ctk.CTkLabel(master=frame_menu, text="Bem-Vindo à Biblioteca!", font=("Roboto", 20, 'bold'), text_color="black", wraplength=230)  # Ajuste de wraplength se necessário
label_titulo.pack(pady=40)

icones = [
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\loanbook.jpeg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\returnbook.jpeg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\listbook.jpeg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\addbook.jpeg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\removebook.jpeg"), size=(20, 20)),
    ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\alunos.jpeg"), size=(20, 20))
]

# Botões do menu com espaçamento simulado por espaços em branco
botoes = ["Novo Empréstimo", "Devolução de Livro", "Todos os Livros", "Adicionar Livro", "Remover Livro", "Alunos"]
comandos = [None, None, show_books, add_book, remove_book, None]

for i in range(len(botoes)):
    botao_frame = ctk.CTkFrame(master=frame_menu, fg_color="#FDFFEC", corner_radius=0)
    botao_frame.pack(fill="x", pady=5)

    botao = ctk.CTkButton(
        master=botao_frame,
        text="      " + str(botoes[i]),  # Adiciona espaços em branco para simular o espaçamento
        font=("Roboto", 16),
        width=260,
        height=40,  # Ajuste a largura para acompanhar a sidebar
        fg_color="#FDFFEC",  # Cor do botão igual à do retângulo
        hover_color="#EEF0D8",  # Cor ao passar o mouse
        corner_radius=0,  # Deixar os botões sem cantos arredondados para uniformidade
        text_color="black",
        anchor="w",  # Alinha o texto à esquerda
        image=icones[i],  # Adiciona o ícone ao botão
        compound="left", # Posiciona o ícone à esquerda do texto
        command=comandos[i]

    )
    botao.pack(fill="x", pady=0)  # Preenchimento horizontal e espaçamento menor entre os botões

# Texto no final do menu
label_credito = ctk.CTkLabel(
    master=frame_menu,
    text="Projeto dos Alunos do ITA para a\nEscola Estadual José Mariotto\nFerreira Aviador (SJC - SP)",
    font=("Roboto", 14),
    text_color="black"
)
label_credito.pack(pady=10, side="bottom")

# Frame principal da tela
frame_principal = ctk.CTkFrame(master=root, fg_color="#F2F2F2")
frame_principal.pack(side="right", expand=True, fill="both")

# Carrega a imagem principal (substitua 'caminho_para_imagem_principal.png' pelo caminho da imagem)
imagem_principal = ctk.CTkImage(light_image=Image.open("C:\\Users\\joao2\\Downloads\\imagemFramePrincipal.jpeg"), size=(500, 500))
label_imagem_principal = ctk.CTkLabel(master=frame_principal, image=imagem_principal, text="")
label_imagem_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem

# Texto no canto inferior direito
label_citacao = ctk.CTkLabel(
    master=frame_principal,
    text="“A educação é a arma mais poderosa que você pode usar para mudar o mundo”\nNelson Mandela",
    font=("Roboto", 16, 'italic'),
    text_color="black",
    justify="left"
)
label_citacao.pack(side="bottom", padx = 20, pady=20, anchor="se")

# Inicializa a interface
root.mainloop()

