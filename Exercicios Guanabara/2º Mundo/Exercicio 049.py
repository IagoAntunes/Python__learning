
#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = float(input("Digite um Numero:"))

for c in range(1,10):
    print(f"{num} + {c} == {num + c}")