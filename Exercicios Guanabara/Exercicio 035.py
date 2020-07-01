
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input("Lado1:"))
l2 = float(input("Lado2:"))
l3 = float(input("Lado3:"))

if(l1 + l2 > l3 and l2 + l3 > l1 and l2 + l3 > l2):
    print("Pode formar um Triangulo!")
else:
    print("Não Podem formar um Triangulo!!")