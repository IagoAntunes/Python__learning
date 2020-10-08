
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input("Digite uma Frase: ")).strip().upper()
palavras = frase.strip()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]

if(inverso == junto):
    print("PALINDROMO")
else:
    print("NÃO É UM PALINDROMO")