
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno_1 = input("Aluno1: ")
aluno_2 = input("Aluno2: ")
aluno_3 = input("Aluno3: ")
aluno_4 = input("Aluno4: ")

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista)

print(f"Ordem de Apresentação: {lista}")