
#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input("Numero:"))
fat = 1
i = num
while(i != 0):
    fat = fat * i
    i = i -1
print(f"FATORIAL = {fat}")