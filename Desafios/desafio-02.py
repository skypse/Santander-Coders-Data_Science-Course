# Autor: Gabriel do Amaral Alves
# Curso: Satander Coders - Data Science
# Data: 15/06/2024
# Aula: Mascara Boleana / Desafio!
# Desafio: Montar uma lista com notas de alunos, implementar uma mascara que mostra os alunos que estão de recuperação,
#  e com isso faça consultas que veja o conjunto de pessoas que foram reprovadas, aprovadas, e quanto precisaria para passar!
import numpy as np
import os


import os
import numpy as np

# Função para limpar o console


def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Criação da lista de notas dos alunos
notas = []

# Loop para coletar 10 notas do usuário
for i in range(10):
    while True:
        limpar_console()  # Limpa o console antes de cada entrada
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

# Converte a lista de notas em um array NumPy
notas_array = np.array(notas)

# Critérios de avaliação
nota_min_aprovacao = 5.0

# Máscaras para identificar os alunos
mascara_aprovados = notas_array >= nota_min_aprovacao
mascara_reprovados = notas_array < nota_min_aprovacao

# trocando aonde não atende os criterios para 'No', oque atende para 'Sim'
resultados_aprovados = np.where(mascara_aprovados, "Yes", "No")
resultados_reprovados = np.where(mascara_reprovados, "Yes", "No")

# Exibe os resultados
limpar_console()

print("Notas dos alunos:", notas_array)
print("Lista de aprovados:", resultados_aprovados)
print("Lista de reprovados:", resultados_reprovados)
