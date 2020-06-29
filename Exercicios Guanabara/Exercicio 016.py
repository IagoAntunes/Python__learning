
#Faça um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira

from math import trunc

n1 = float(input("Digite um Numero: "))

print(f"Porção Inteira: {trunc(n1)}")