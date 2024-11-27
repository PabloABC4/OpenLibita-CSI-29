# Modularização de Funções

Para cada botão do menu principal, ao invés de as respectivas funções estarem no próprio arquivo da interface, cada função possui um arquivo próprio para maior organização e entendimento do presente código. A seguir, uma lista de todas as funções:

## main_menu.py

Exibe a tela principal do Programa, mostrando todas as funcionalidades abaixo pelos botões à esquerda:

```
Adição de empréstimos (add_loan.py)
Conclusão de empréstimos (end_loan.py)
Adição de livros (add_book.py)
Remoção de livros (remove_book.py)
Consulta de empréstimos por aluno (show_students.py)
```

## backend.py

O único arquivo que consegue estabelecer contato com o Banco de Dados, realizando as seguintes _queries_ conforme operações do usuário:

```
Obtenção dos livros do banco de dados (get_books)
Obtenção dos estudantes cadastrados no banco de dados (get_students)
Adição de livro (add_book)
Remoção de livro (remove_book)
Adição de empréstimo (add_loan)
Obtenção dos empréstimos (get_loans)
Conclusão de empréstimos (end_loan)
Obtenção de empréstimos por estudante (get_student_loans)
```

## add_book.py

Adiciona um livro ao sistema.

### São necessários:

```
Título da Obra
Nome da Editora
```

## add_loan.py

Adiciona um empréstimo ao sistema.

### São necessários:

```
ID do Aluno Receptor
ID do Livro Emprestado
data de Empréstimo
data de Devolução Prevista
```

## end_loan.py

Retira-se um empréstimo do sistema, exibindo na tela todos os empréstimos do banco de dados ainda não finalizados.

### São necessários:

```
ID do Empréstimo
Data Real de Devolução
```

## remove_book.py

Retira-se um livro do sistema, exibindo na tela todos os livros do banco de dados

### São necessários:

```
ID do Livro
```

## show_students.py

Mostra todos os estudantes cadastrados na biblioteca. É possível também pesquisar um aluno e exibir seus empréstimos
