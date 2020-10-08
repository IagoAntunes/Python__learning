
#Faça um programa que leia o comprimento do cateto oposto e do adjacente
#de um triangulo retangulo.Calcule e mostre a hipotenusa

import math
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))

hipotenusa = math.sqrt(co**2 + ca**2)

print(f"Hipotenusa: {hipotenusa}")