# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy / Desafio!
# Desafio: Escrever programa que o usuario digite 10 numeros,
# sendo notas de alunos, transforma em array do numpy e faz os calculos como: Max, Min, Std, Mean, Argmin...

import numpy as np

print("Insira as notas dos alunos!")

notas = []

for n in range(10):
    while True:
        try:
            # Solicitar nota
            nota = float(input(f"Digite a nota do aluno {n + 1}: "))
            # Append na lista
            notas.append(nota)
            break
        except ValueError:
            print("Insira um valor númerico válido!")

# Convertendo a Lista em uma Array Numpy
lista_de_notas_array = np.array(notas)
print("Array de notas:", lista_de_notas_array)
