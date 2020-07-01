
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input("Salário:"))
if(salario > 1250):
    aumento = (salario * 10)/100
else:
    aumento = (salario * 15)/100
print(f"\nAumento:{aumento} \nNovo Salario:{salario + aumento}")