# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Mascara Boleana

import numpy as np

# Criando uma array de notas
notas = np.array([4.9, 6.5, 3.5, 6.9])

mask_notas = notas >= 5
print("Array de notas puxando somente os aprovados:")
print(mask_notas)  # [False  True False  True]
