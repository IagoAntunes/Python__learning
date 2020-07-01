
#Faça um programa que leia um salário de um funcionario e mostre
# seu novo salario com 15% de aumento

salario = float(input("Digite o Salário:"))

aumento = (salario * 15)/100

print(f"Aumento: {aumento} \nSalario: {salario + aumento}")