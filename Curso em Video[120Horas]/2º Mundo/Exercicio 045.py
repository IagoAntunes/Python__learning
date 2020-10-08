
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

lista = ['PEDRA','PAPEL','TESOURA']
computador = choice(lista)

usuario = str(input("Escolha:")).upper()
print(f"\nVocê Jogou....{usuario}")
print(f"Computador Jogou...{computador}")

if(computador == lista[0] and usuario == lista[2]):
    print("COMPUTADOR WIN")
elif(computador == lista[0] and usuario == lista[0]):
    print("EMPATE")
elif(computador == lista[0] and usuario == lista [1]):
    print("VOCE GANHOU")

elif(computador == lista[1] and usuario == lista[2]):
    print("VOCE GANHOU")
elif(computador == lista[1] and usuario == lista [0]):
    print("COMPUTADOR WIN")
elif(computador == lista[1] and usuario == lista[1]):
    print("EMPATE")

elif(computador == lista[2] and usuario == lista[2]):
    print("EMPATE")
elif(computador == lista[2] and usuario == lista [0]):
    print("VOCE GANHOU")
elif(computador == lista[2] and usuario == lista[1]):
    print("COMPUTADOR WIN")