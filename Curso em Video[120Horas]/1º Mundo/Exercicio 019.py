# Um professor que sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele lendo o nome deles,e escrevendo o escolhido.

import random

aluno_1 = input("Aluno1: ")
aluno_2 = input("Aluno2: ")
aluno_3 = input("Aluno3: ")
aluno_4 = input("Aluno4: ")

lista = [aluno_1,aluno_2,aluno_3,aluno_4]
escolhido = random.choice(lista)

print(f"O escolhido foi {escolhido}")