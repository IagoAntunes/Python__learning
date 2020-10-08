
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input("Numero1:"))
n2 = float(input("Numero2:"))
n3 = float(input("Numero3:"))

if(n1 > n2 and n2 > n3):
    maior = n1
    menor = n3
if(n1 > n3 and n3 > n2):
    maior = n1
    menor = n2
if(n2 > n1 and n1 > n3):
    maior = n2
    menor = n3
if(n2 > n3 and n3 > n1):
    maior = n2
    menor = n1
if(n3 > n2 and n2 > n1):
    maior = n3
    menor = n1
if(n3 > n1 and n1 > n2):
    maior = n3
    menor = n2

print(f"\nMaior:{maior} \nMenor:{menor}")