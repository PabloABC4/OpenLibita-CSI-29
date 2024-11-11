# OpenLibita

## Introdução
OpenLibita é um sistema desenvolvido para digitalizar e otimizar a gestão de bibliotecas de pequeno e médio porte, com um foco especial em escolas públicas que ainda utilizam métodos manuais para controlar seus acervos. O projeto busca tornar essa gestão mais intuitiva e acessível, permitindo que professores, coordenadores e outros responsáveis possam realizar operações voltadas ao gerenciamento de biblioteca de forma simples e eficiente.

## Equipe de Desenvolvimento
O presente projeto foi criado por um grupo de alunos graduandos em Engenharia da Computação pelo Instituto Tecnológico de Aeronáutica (ITA), da turma de 2026, como entregável principal da disciplina de CSI-28: Fundamentos de Engenharia de Software.

A seguir, a lista dos alunos contribuintes do projeto:

- João Victor Bezerra Cavalcante
- Lean Kaique Cardoso de Souza
- Marcelo Loiola Lopes Veras
- Pablo Augusto Brigagão
- Suellen Marina de Almeida

## Objetivos do Projeto
O principal objetivo do OpenLibita é oferecer funcionalidades básicas e essenciais para o controle de bibliotecas, incluindo:
- Cadastro de livros por ISBN
- Consulta de obras por tópicos, nome do autor, título, entre outros critérios
- Gestão de exemplares disponíveis
- Gerenciamento de empréstimos e prazos de devolução
- Cadastro e remoção de usuários

## Área de Aplicação
O software é voltado para bibliotecas de pequeno e médio porte, idealmente com até 2.000 exemplares. A proposta inicial é aplicá-lo em escolas públicas, mas seu uso pode ser estendido a outras áreas, como coleções pessoais e pequenas instituições.

## Funcionalidades
### Requisitos Funcionais
Os principais requisitos funcionais do OpenLibita incluem:
- **RF01**: O usuário deve conseguir consultar a quantidade de exemplares de um livro.
- **RF02**: O usuário deve poder criar um empréstimo no software.
- **RF03**: O usuário deve poder associar o nome de um aluno a um empréstimo.
- **RF04**: O usuário deve poder associar o nome do livro, assunto, editora e código a um empréstimo.
- **RF05**: O usuário deve poder inserir datas de empréstimo e devolução.
- **RF06**: O usuário deve poder cadastrar novos livros no sistema.
- **RF07**: O usuário deve poder consultar a quantidade de livros utilizados por um aluno.

### Requisitos Não Funcionais
- **NF01**: A quantidade de livros emprestados por um aluno deve ser armazenada.
- **NF02**: A quantidade de exemplares de um livro deve ser atualizada após um empréstimo.

## Estrutura de Banco de Dados
O banco de dados do OpenLibita é projetado para suportar as funcionalidades mencionadas acima, com as seguintes tabelas principais:
- **Livro**: (id_livro, num_edicao, num_exemplar, volume, titulo)
- **Editora**: (id_editora, nome_editora)
- **Assunto**: (id_assunto, nome_assunto)
- **Doador**: (id_doador, nome_doador, data_doacao, cpf_doador)
- **Localização**: (id_localizacao, corredor, prateleira, andar, estante)
- **Autor**: (id_autor, nome_autor)
- **Usuário**: (id_usuario, identidade_usuario, email_usuario, telefone_trabalho, telefone_celular, ramal_usuario, cpf_usuario, nome_usuario)
- **Tipo**: (id_tipo_usuario, nome_tipo_usuario)
- **Empréstimo**: (data_emprestimo, data_prevista_devolucao, data_devolucao)

## Tecnologias Utilizadas
- **Linguagem de Programação Principal**: Python
- **Interface Gráfica**: Biblioteca `Tkinter`
- **Banco de Dados**: SQL Server, acessado por meio da biblioteca `pyodbc`
- **Frameworks e Ferramentas**: SSMS para gerenciamento do servidor de banco de dados

<!-- ## Como Executar o Projeto
1. Certifique-se de que o Python e o driver ODBC para SQL Server estão instalados.
2. Clone o repositório do projeto.
3. Configure as credenciais de conexão com o banco de dados no arquivo Python principal.
4. Execute o script para verificar a conectividade e listar as tabelas disponíveis:
    ```python
    import pyodbc

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=SEU_SERVIDOR;'
        'DATABASE=Library;'
        'Trusted_Connection=yes;'
    )

    cursor = conn.cursor()
    cursor.execute('SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = \'BASE TABLE\';')
    for row in cursor.fetchall():
        print(row.TABLE_NAME)
    
    conn.close()
    ``` -->

## Considerações Finais
O OpenLibita é um projeto de software livre, desenvolvido com o objetivo de atender à demanda de gerenciamento de bibliotecas escolares, mas também adaptável para outras aplicações similares. Funcionalidades futuras e melhorias serão implementadas conforme o feedback dos usuários e as necessidades adicionais surgirem.

---
