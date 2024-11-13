import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

def get_connection():
    return pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={os.getenv("DB_SERVER")};'
        f'DATABASE={os.getenv("DB_NAME")};'
        f'Trusted_Connection={os.getenv("DB_TRUSTED_CONNECTION")};'
    )

def get_books():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Livros')
        books = cursor.fetchall()
        conn.close()
        return books
    except Exception as e:
        return str(e)

def add_book(title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Livros (titulo, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                       (title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)

def remove_book(book_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Livros WHERE id_livro = ?', (book_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)

def add_loan(id_usuario, id_livro, data_emprestimo, data_prevista_devolucao):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Emprestimos (id_usuario, id_livro, data_emprestimo, data_prevista_devolucao) VALUES (?, ?, ?, ?)', 
                       (id_usuario, id_livro, data_emprestimo, data_prevista_devolucao))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)
    
def get_loans():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Emprestimos')
        books = cursor.fetchall()
        conn.close()
        return books
    except Exception as e:
        return str(e)
    
def end_loan(loan_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Emprestimos WHERE id_emprestimo = ?', (loan_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)
