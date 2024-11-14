-- Tabela Usuários
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY IDENTITY(1,1),
    identidade_usuario NVARCHAR(20),
    email_usuario NVARCHAR(255),
    telefone_trabalho NVARCHAR(15),
    telefone_celular NVARCHAR(15),
    ramal_usuario NVARCHAR(5),
    cpf_usuario NVARCHAR(15) UNIQUE,
    nome_usuario NVARCHAR(255) NOT NULL
);

-- Tabela Editoras
CREATE TABLE Editoras (
    id_editora INT PRIMARY KEY IDENTITY(1,1),
    nome_editora NVARCHAR(255) NOT NULL
);

-- Tabela Assuntos
CREATE TABLE Assuntos (
    id_assunto INT PRIMARY KEY IDENTITY(1,1),
    nome_assunto NVARCHAR(255) NOT NULL
);

-- Tabela Doadores
CREATE TABLE Doadores (
    id_doador INT PRIMARY KEY IDENTITY(1,1),
    nome_doador NVARCHAR(255) NOT NULL,
    data_doacao DATE NOT NULL,
    cpf_doador NVARCHAR(15) UNIQUE
);

-- Tabela Localização
CREATE TABLE Localizacao (
    id_localizacao INT PRIMARY KEY IDENTITY(1,1),
    corredor NVARCHAR(10),
    prateleira NVARCHAR(10),
    andar NVARCHAR(5),
    estante NVARCHAR(10)
);

-- Tabela Autores
CREATE TABLE Autores (
    id_autor INT PRIMARY KEY IDENTITY(1,1),
    nome_autor NVARCHAR(255) NOT NULL
);

-- Tabela Tipo de Usuário
CREATE TABLE Tipo (
    id_tipo_usuario INT PRIMARY KEY IDENTITY(1,1),
    nome_tipo_usuario NVARCHAR(255) NOT NULL
);

-- Tabela Livros
CREATE TABLE Livros (
    id_livro INT PRIMARY KEY IDENTITY(1,1),
    titulo NVARCHAR(255) NOT NULL,
    num_edicao INT,
    num_exemplar INT,
    volume NVARCHAR(50),
    id_editora INT,
    id_assunto INT,
    id_localizacao INT,
    FOREIGN KEY (id_editora) REFERENCES Editoras(id_editora),
    FOREIGN KEY (id_assunto) REFERENCES Assuntos(id_assunto),
    FOREIGN KEY (id_localizacao) REFERENCES Localizacao(id_localizacao)
);

-- Tabela Empréstimos
CREATE TABLE Emprestimos (
    id_emprestimo INT PRIMARY KEY IDENTITY(1,1),
    id_usuario INT,
    id_livro INT,
    data_emprestimo DATE NOT NULL,
    data_prevista_devolucao DATE,
    data_devolucao DATE,
    finalizado BIT DEFAULT 0,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_livro) REFERENCES Livros(id_livro)
);
