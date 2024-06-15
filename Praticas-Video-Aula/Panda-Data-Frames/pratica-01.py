# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Panda DataFrames

import pandas as pd

# Criando um dicionario com autores, precos e titulos
dicionario = {"Autores": ["Rick Riordan", "J. R. R. Tolkiem", "Rick Riordan", "Machado de Assis"],
              "Titulos": ["O Ladrão de Raios", "A Sociedade do Anel", "Mar de Monstros", "Memórias Postumas de Brás Cubas"],
              "Preços": [41.2, 35.7, 39.5, 40.5]}

# Data Frame
df = pd.DataFrame(dicionario)
print(df)