
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input("Sexo: [M]Masculino [F]Feminino : ")).upper()
while(sexo != 'M' and sexo != 'F'):
    print("Dados Invalidos")
    sexo = str(input("Sexo: [M]Masculino [F]Feminino : "))