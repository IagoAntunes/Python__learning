
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
m = 0
maior = 0
Midade = 0
for c in range(1,5):
    nome = str(input(f"\nNome{c}: "))
    idade = int(input(f"Idade{c}: "))
    sexo = int(input(f"Sexo{c} [1]Homen [2]Mulher : "))
    if(sexo == 1 and idade > maior):
        maior = idade
        nomeS = nome
    if(sexo == 2 and idade < 20):
        m += 1

    Midade +=idade

print(f"MEDIA DE IDADE:{Midade/4}")
print(f"Homem Mais velho:{nomeS} Idade = {maior}")
print(f"Mulheres com Idade menor que 20: {m}")