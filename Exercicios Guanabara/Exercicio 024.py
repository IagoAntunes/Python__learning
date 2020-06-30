
#Crie um Programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = input("Nome da Cidade:").strip()
dividido = cidade.split()
print(f"{'Santo' in dividido[0]}")