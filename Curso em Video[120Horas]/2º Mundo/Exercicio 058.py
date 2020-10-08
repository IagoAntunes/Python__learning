
#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
tent = 1
computador = randint(0,10)
usuario = int(input("Digite um Numero:"))

if(usuario == computador):
    print("Você Acertou!!!")
else:
    while(usuario != computador):
        if(computador > usuario):
            print("Chute um Numero Maior")
        else:
            print("Chute um Numero Menor")
        usuario = int(input("Digite um Numero:"))
        tent += 1
        if(usuario == computador):
            print("Você Acertou!!")
print(f"Numero de Tentativas: {tent}")
