
#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre eles
soma = 0
qnt=0
num = 0
while(num != 999):
    num = int(input("Digite um Numero:"))
    qnt += 1
    soma+=num

print(f"Numeros Digitados:{qnt}")
print(f"Soma={soma-999}")