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
        cursor.execute('SELECT id_livro, titulo, editora, em_emprestimo FROM Livros WHERE existente = 1')
        books = cursor.fetchall()
        columns = [column[0] for column in cursor.description if column[0] != 'existente']
        conn.close()
        return books, columns
    except Exception as e:
        return str(e), []

def get_students():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id_aluno, nome_aluno, email_aluno, telefone_celular FROM Alunos')
        students = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        conn.close()
        return students, columns
    except Exception as e:
        return str(e), []

def add_book(title, editora):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Livros (titulo, editora) OUTPUT INSERTED.id_livro VALUES (?, ?)', 
                       (title, editora))
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
        
        # Check if the book is currently on loan
        cursor.execute('SELECT 1 FROM Emprestimos WHERE id_livro = ? AND finalizado = 0', (book_id,))
        active_loan = cursor.fetchone()
        
        if active_loan:
            conn.close()
            return "Esse livro não pode ser removido pois está sendo emprestado."
        
        cursor.execute('UPDATE Livros SET existente = 0 WHERE id_livro = ?', (book_id,))
        conn.commit()
        conn.close()
        return None
    except Exception as e:
        return str(e)

def add_loan(id_aluno, id_livro, data_emprestimo, data_prevista_devolucao):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM Livros WHERE id_livro = ?', (id_livro,))
        if cursor.fetchone()[0] == 0:
            return "ID de livro inválido"
        
        cursor.execute('SELECT em_emprestimo, existente FROM Livros WHERE id_livro = ?', (id_livro,))
        livro_status = cursor.fetchone()
        if not livro_status[1]:
            return "Livro removido da biblioteca"
        if livro_status[0]:
            return "Esse livro já está sendo emprestado"
        
        cursor.execute('INSERT INTO Emprestimos (id_aluno, id_livro, data_emprestimo, data_prevista_devolucao) OUTPUT INSERTED.id_emprestimo VALUES (?, ?, ?, ?)', 
                       (id_aluno, id_livro, data_emprestimo, data_prevista_devolucao))
        loan_id = cursor.fetchone()[0]
        
        cursor.execute('UPDATE Livros SET em_emprestimo = 1 WHERE id_livro = ?', (id_livro,))
        
        conn.commit()
        conn.close()
        return loan_id
    except Exception as e:
        return str(e)
    
def get_loans():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id_emprestimo, id_aluno, id_livro, data_emprestimo, data_prevista_devolucao, finalizado FROM Emprestimos WHERE finalizado = 0')
        loans = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        conn.close()
        return loans, columns
    except Exception as e:
        return str(e), []
    
def end_loan(loan_id, loan_end_date):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Emprestimos SET finalizado = 1, data_devolucao = ? WHERE id_emprestimo = ?', (loan_end_date, loan_id))
        cursor.execute('UPDATE Livros SET em_emprestimo = 0 FROM Livros JOIN Emprestimos ON Livros.id_livro = Emprestimos.id_livro WHERE Emprestimos.id_emprestimo = ?', (loan_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        return str(e)

def get_student_loans(student_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id_emprestimo, id_livro, data_emprestimo, data_prevista_devolucao, data_devolucao, finalizado FROM Emprestimos WHERE id_aluno = ?', (student_id,))
        loans = cursor.fetchall()
        conn.close()
        return loans
    except Exception as e:
        return str(e)
