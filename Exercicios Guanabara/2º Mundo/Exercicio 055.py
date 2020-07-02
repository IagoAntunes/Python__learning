
#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = -10
menor = 90
for c in range(1,6):
    peso = float(input(f"Peso Pessoa{c}: "))
    if(peso > maior):
        maior = peso
    if(peso < menor):
        menor = peso

print(f"Maior Peso: {maior} \nMenor Peso: {menor}")