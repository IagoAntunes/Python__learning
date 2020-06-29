
#Faça um programa que leia a largura e altura de uma parede em metros.
#Calcule a sua area e a quantidade de tinta necessaria para pinta-la
#Sabendo que cada litro de tinta pinta uma area de 2m²

altura = float(input("Altura:"))
largura = float(input("Largura:"))

area = altura * largura

print(f"Quantidade de Tinta necessaria: {area/2}")