
#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Ano de Nascimento: "))
idade = 2020 - ano
if(idade == 18):
    print("Você Deve se Alistar esse Ano!")
elif(idade > 18):
    print("Seu tempo de Alistamento já passou!")
    print(f"Você Deveria ter se alistado á {idade - 18} anos")
elif(idade < 18):
    print(f"Você tera que se alistar daqui {18 - idade} anos")