# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy

import numpy as np

# Criando uma lista e transformando em uma lista do numpy:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = np.array(lista)
print(lista) # Lista Padrão: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array) # Lista Numpy: [ 1  2  3  4  5  6  7  8  9 10]
print(type(lista)) # Type lista Padrão: <class 'list'>
print(type(array)) # Type lista Numpy: <class 'numpy.ndarray'>

