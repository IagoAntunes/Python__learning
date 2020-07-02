
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input("Valor da Casa: "))
salario = float(input("Salário: "))
anos = int(input("Anos: "))

mensal = vcasa / (anos * 12)
salario2 = salario * 30 /100

if(mensal > salario2):
    print("EMPRESTIMO NEGADO!")
else:
    print("EMPRESTIMO APROVADO!")
print(f"\nValor Mensal: R$ {mensal}  ",end='')
print(f"Numero de Anos: {anos}")