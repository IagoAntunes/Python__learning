
#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário,
# 2 para octal e 3 para hexadecimal.

num = int(input("Numero: "))

print("Base de Conversão:")
opcao = int(input(("[1]Binario \n[2]Octal \n[3]Hexadecimal \n")))

if(opcao==1):
    print(f"{num} para Binario = {bin(num)[2:]}")
elif(opcao==2):
    print(f"{num} para Octal = {oct(num)[2:]}")
elif(opcao==3):
    print(f"{num} para hexadecimal = {hex(num)[2:]}")
else:
    print("OPCAO INVALIDA!!")
