# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Analisando Dados

import pandas as pd

peoples = pd.read_csv("./people-100.csv")
peoples.head()

# Selecionando colunas:
peoples.columns

# Profissões comuns nesse dataset:
profissoes_comuns = peoples["Job Title"].value_counts()

# Exibindo profissoes comuns:
print(profissoes_comuns)

# Pegando o total de pessoas:
total_pessoas = peoples.shape[0]

# Exibindo total pessoas:
print(total_pessoas)