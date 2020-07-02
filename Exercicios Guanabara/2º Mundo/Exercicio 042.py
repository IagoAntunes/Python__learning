
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais    ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

l1 = float(input("Lado1: "))
l2 = float(input("Lado2: "))
l3 = float(input("Lado3: "))

if(l1 == l2 and l2 == l3):
    print("TRIANGULO EQUILATERIO")
elif(l1 == l2 or l1 == l3 or l2 == l3):
    print("TRIANGULO ISÓSCELES")
elif(l1 != l2 and l1 != l3 and l2 != l3):
    print("TRIANGULO ESCALENO")