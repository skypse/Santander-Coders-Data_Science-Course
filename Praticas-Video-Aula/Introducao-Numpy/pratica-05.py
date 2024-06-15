# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy

import numpy as np

# Matriz com Numpy
matriz_zeros = np.zeros((5, 3))
print("Matriz sem alterações:")
print(matriz_zeros)
print("--------------------------------------------------")

# Alterar um valor na posição [3, 1] (quarta linha segunda coluna)
matriz_zeros[3, 1] = 99
print("Matriz após alterar o valor na posição [2, 1]:")
print(matriz_zeros)
