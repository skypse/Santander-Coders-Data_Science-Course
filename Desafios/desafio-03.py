# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Panda DataFrames / Desafio!
# Desafio: Montar uma tabela, contendo livros, autores e adicione um livro novo!

import pandas as pd

# Criar um DataFrame inicial com livros e autores
data = {
    'Livro': ['Harry Potter e a Pedra Filosofal', 'O Senhor dos Anéis', 'O Hobbit'],
    'Autor': ['J.K. Rowling', 'J.R.R. Tolkien', 'J.R.R. Tolkien']
}
df = pd.DataFrame(data)
print('--------------------------------------------------------')
print("Tabela inicial de livros e autores:")
print(df)

# Adicionando o novo livro ao DataFrame em uma única linha
df = pd.concat([df, pd.DataFrame(
    [{'Livro': 'Percy Jackson e o Ladrão de Raios', 'Autor': 'Rick Riordan'}])], ignore_index=True)

print('--------------------------------------------------------')
print("Tabela após adicionar um novo livro:")
print(df)
print('--------------------------------------------------------')
