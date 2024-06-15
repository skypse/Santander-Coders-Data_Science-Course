# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy

import numpy as np

# Notas de alunos:
lista_de_notas = [9.5, 7.1, 6.5, 5.6, 9.1, 7.8]
notas = np.array(lista_de_notas)
print("Máximo de notas", notas.max())  # Nota máximoa
print("Mínimo de notas", notas.min())  # Nota mínima
print("Desvio Padrão", notas.std())  # Desvio Padrão
print("Média de notas", notas.mean())  # Média
print("Posição da menor nota", notas.argmin())  # Posição do menor valor
print("Posição da maior nota", notas.argmax())  # Posição do maior valor
