
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

usuario = int(input("Adivinhe o Numero.(1 a 5)"))
numero = randint(1,5)

if(usuario == numero):
    print("PARABENS VOCE ACERTOU")
else:
    print(f"Tente Novamente! \nNumero:{numero}")
