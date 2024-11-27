-- Tabela Alunos
CREATE TABLE Alunos (
    id_aluno INT PRIMARY KEY IDENTITY(1,1),
    nome_aluno NVARCHAR(255),
    email_aluno NVARCHAR(255),
    telefone_celular NVARCHAR(15),
);

-- Tabela Livros
CREATE TABLE Livros (
    id_livro INT PRIMARY KEY IDENTITY(1,1),
    titulo NVARCHAR(255) NOT NULL,
    editora NVARCHAR(255),
    em_emprestimo BIT DEFAULT 0,
    existente BIT DEFAULT 1
);

-- Tabela Empréstimos
CREATE TABLE Emprestimos (
    id_emprestimo INT PRIMARY KEY IDENTITY(1,1),
    id_aluno INT,
    id_livro INT,
    data_emprestimo DATE,
    data_prevista_devolucao DATE,
    data_devolucao DATE DEFAULT NULL,
    finalizado BIT DEFAULT 0,
    FOREIGN KEY (id_aluno) REFERENCES Alunos(id_aluno),
    FOREIGN KEY (id_livro) REFERENCES Livros(id_livro)
);
