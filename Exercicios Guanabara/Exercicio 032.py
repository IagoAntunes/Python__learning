
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um Ano:"))

if(ano % 4 == 0):
    if(ano % 100 != 0):
        print("É BISSEXTO")
else:
    print("Não é Bissexto")