
#Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida
#o primeiro e o ultimo nome separadamente

nome = input("Nome Completo:")
dividido = nome.split()

print(f"Primeiro Nome: {dividido[0]}")
print(f"Ultimo Nome: {dividido[-1]}")