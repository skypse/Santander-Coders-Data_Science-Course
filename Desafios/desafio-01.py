# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Introdução ao Numpy / Desafio!
# Desafio: Escrever programa que o usuario digite 10 numeros,
# sendo notas de alunos, transforma em array do numpy e faz os calculos como: Max, Min, Std, Mean, Argmin...

import numpy as np
import os


def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


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

limpar_console()

# Convertendo a Lista em uma Array Numpy
lista_de_notas_array = np.array(notas)
print("Maior nota da lista:", lista_de_notas_array.max())
print("Menor nota da lista:", lista_de_notas_array.min())
print("Media das notas:", lista_de_notas_array.mean())
print("Desvio Padrão da lista:", lista_de_notas_array.std())
print("Posição da maior nota da lista:", lista_de_notas_array.argmax())
print("Posição da menor nota da lista:", lista_de_notas_array.argmin())
print("Array de notas:", lista_de_notas_array)
