
#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input("Digite um Numero: "))
razao = int(input("Razão: "))
decimo = num + (10 - 1) * razao

while(num <decimo):
    num = num + razao
    print(num)
