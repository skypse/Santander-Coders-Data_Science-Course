# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy

import numpy as np

# Criando uma Array de zeros com Numpy
array_de_zeros = np.zeros(10)
print(array_de_zeros) # Lista criada com zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Alterando o dado referente a posição
array_de_zeros[0] = 9
print(array_de_zeros[0]) # = 9.0
print(array_de_zeros) # Chamando a lista pós alteração: [9. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
