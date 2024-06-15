# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Panda Series

import pandas as pd

notas = {'Gabriel': 8, 'Moner': 6.5, 'Virginio': 5.4}
serie_notas = pd.Series(notas)
print(serie_notas)

print(serie_notas.mean())
print(serie_notas.median())
print(serie_notas.describe())
