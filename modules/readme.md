# Modularização de Funções

Para cada botão do menu principal, ao invés de as respectivas funções estarem no próprio arquivo da interface, cada função possui um arquivo próprio para maior organização e entendimento do presente código. A seguir, uma lista de todas as funções:

## add_book.py

Adiciona um livro ao sistema.

### São necessários:

```
Título
Número da Edição
Número de Exemplar
Volume
ID de Editora
ID de Assunto
ID de Localização
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

Mostra todos os estudantes cadastrados na biblioteca.
