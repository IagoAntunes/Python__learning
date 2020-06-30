
#Faça um programa que leia o nome completo de uma pessoa e mostre:
#-Nome com todas as letras maiusculas.
#-Nome com todas letras minusculas
#-Quantas letras ao todos,sem consierar os espaços
#-Quantas letras tem o primeiro nome

nome=input("Digite Seu Nome:").strip()

dividido = nome.split()

print(f"Nome Maiusculo: {nome.upper()} \nNome Minusculo: {nome.lower()}")
print(f"Letras Ao Todo:{len(nome) - nome.count(' ')} \nLetras 1ºNome: {len(dividido[0])}")