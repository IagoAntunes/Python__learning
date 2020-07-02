
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM   -Até 14 anos: INFANTIL -Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR   Acima de 25 anos: MASTER

ano = int(input("Ano de Nascimento: "))
idade = 2020 - ano

if(idade < 9):
    print("Categoria MIRIM")
elif(idade < 14):
    print("Categoria INFANTIL")
elif(idade < 19):
    print("Categoria JÚNIOR")
elif(idade < 25):
    print("Categoria SENIOr")
elif(idade > 25):
    print("Categoria MASTER")