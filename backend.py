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
        columns = [column[0] for column in cursor.description]
        conn.close()
        return books, columns
    except Exception as e:
        return str(e), []
    
def get_students():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Usuarios')
        students = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        conn.close()
        return students, columns
    except Exception as e:
        return str(e), []

def add_book(title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Livros (titulo, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao) OUTPUT INSERTED.id_livro VALUES (?, ?, ?, ?, ?, ?, ?)', 
                       (title, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao))
        book_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return book_id
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
        
        cursor.execute('SELECT disponibilidade FROM Livros WHERE id_livro = ?', (id_livro,))
        disponibilidade = cursor.fetchone()[0]
        if disponibilidade == "Indisponível":
            return disponibilidade

        
        cursor.execute('INSERT INTO Emprestimos (id_usuario, id_livro, data_emprestimo, data_prevista_devolucao) OUTPUT INSERTED.id_emprestimo VALUES (?, ?, ?, ?)', 
                       (id_usuario, id_livro, data_emprestimo, data_prevista_devolucao))
        loan_id = cursor.fetchone()[0]
        
        cursor.execute('UPDATE Livros SET disponibilidade = ? WHERE id_livro = ?', ('Indisponível', id_livro))
        
        conn.commit()
        conn.close()
        return loan_id
    except Exception as e:
        return str(e)
    
def get_loans():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Emprestimos WHERE finalizado = 0')
        loans = cursor.fetchall()
        conn.close()
        return loans
    except Exception as e:
        return str(e)
    
def end_loan(loan_id, loan_end_date):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Emprestimos SET finalizado = 1, data_devolucao = ? WHERE id_emprestimo = ?', (loan_end_date, loan_id))
        cursor.execute('UPDATE Livros SET disponibilidade = ? FROM Livros JOIN Emprestimos ON Livros.id_livro = Emprestimos.id_livro WHERE Emprestimos.id_emprestimo = ?', ('Disponível', loan_id))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)
