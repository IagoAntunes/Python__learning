# Faça um programa que leia algo pela tela do seu computador e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ela

n1 = input("Digite um Numero: ")

print(f"É uma Letra: {n1.isalpha()}")
print(f"É um Numero: {n1.isnumeric()}")
print(f"É um Decimal: {n1.isdecimal()}")
print(f"É Minusculo: {n1.islower()}")


