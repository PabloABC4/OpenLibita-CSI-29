INSERT INTO Editoras (nome_editora) VALUES
('Editora A'),
('Editora B'),
('Editora C');

INSERT INTO Assuntos (nome_assunto) VALUES
('Ficção Científica'),
('História'),
('Matemática'),
('Literatura Clássica');

INSERT INTO Doadores (nome_doador, data_doacao, cpf_doador) VALUES
('Carlos Silva', '2024-01-15', '12345678900'),
('Maria Oliveira', '2024-02-10', '98765432100'),
('João Santos', '2024-03-05', '45612378900');

INSERT INTO Localizacao (corredor, prateleira, andar, estante) VALUES
('A1', 'P1', '1', 'E1'),
('B2', 'P3', '2', 'E4'),
('C3', 'P2', '1', 'E5');

INSERT INTO Autores (nome_autor) VALUES
('Júlio Verne'),
('Machado de Assis'),
('Albert Einstein'),
('Isaac Newton');

INSERT INTO Usuarios (identidade_usuario, email_usuario, telefone_trabalho, telefone_celular, ramal_usuario, cpf_usuario, nome_usuario) VALUES
('RG123456', 'ana.silva@biblioteca.com', '123456789', '987654321', '101', '11122233344', 'Ana Silva'),
('RG789012', 'joao.pereira@biblioteca.com', '987654321', '123456789', '102', '55566677788', 'João Pereira'),
('RG345678', 'maria.souza@biblioteca.com', '456123789', '789123456', '103', '99988877766', 'Maria Souza');

INSERT INTO Tipo (nome_tipo_usuario) VALUES
('Aluno'),
('Professor'),
('Visitante');

INSERT INTO Livros (titulo, num_edicao, num_exemplar, volume, id_editora, id_assunto, id_localizacao) VALUES
('Viagem ao Centro da Terra', 1, 5, 'Volume Único', 1, 1, 1),
('Dom Casmurro', 2, 3, 'Volume Único', 2, 4, 2),
('Relatividade: A Teoria Especial e Geral', 1, 4, 'Volume Único', 3, 3, 3);