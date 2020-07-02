
# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

par = 0
for c in range(1,7):
    num = int(input(f"Numero{c} :"))
    if(num % 2 == 0):
        par = par + num
print(f"SOMA = {par}")
