
#Faça um programa que leia uma frase e mostre:
#-Quantas veses aparece a letra 'A'
#-Em que posição ela aparece pela primeira vez
#-Em que posição ela aparece a ultima vez

frase = input("Digite uma Frase:")

print(f"A aparece {frase.count('A')}vezes")
print(f"Posicao: {frase.find('A')}")
print(f"Ultima Posicao: {frase.rfind('A')}")