
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from math import trunc

n1 = int(input("Digite um Numero: "))
metade = trunc(n1/2)
primo = 0
for c in range(1,metade):
    if(n1 % c == 0):
        primo = primo + 1
if ( primo == 1):
    print("NUMERO PRIMO")
else:
    print("NÃO É PRIMO")