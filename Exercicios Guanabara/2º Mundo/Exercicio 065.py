
#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

qnt= 0
menor = 0
maior = 0
total = 0
opcao = 's'
while(opcao != 'não'):
    num = int(input("Digite um Numero:"))
    total += num
    qnt += 1
    if(num > maior):
        maior = num
    if(num < menor):
        menor = num
    opcao = str(input("Deseja Continuar ?")).lower()
print(f"Media = {total/qnt}")
print(f"Maior Valor:{maior} \nMenor Valor:{menor}")

