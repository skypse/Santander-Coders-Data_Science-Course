# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Mascara Boleana

import numpy as np

# Criando array string, se é positivo ou não
print("Array Padrão:")
is_covid_positive = np.array(['Yes', 'No', 'No', 'Yes', 'No'])
print(is_covid_positive)

# Criando uma mask para == 'Yes'
mask = (is_covid_positive == 'Yes')

# Tudo que vier como 'Yes' mudar para 'C19' de Covid-19
print("------------------------------------------")
print("Array com as alterações da mascara:")
is_covid_positive[mask] = 'C19'
print(is_covid_positive) # ['C19' 'No' 'No' 'C19' 'No']
