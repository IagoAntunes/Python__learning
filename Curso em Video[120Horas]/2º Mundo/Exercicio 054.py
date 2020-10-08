
#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input("Ano de Nascimento: "))
    idade = 2020 - ano
    if(idade >= 18):
        maior += 1
    else:
        menor += 1

print(f"Maiores de Idade: {maior} \nMenores de Idade: {menor}")