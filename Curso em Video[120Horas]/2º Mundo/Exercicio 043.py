
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC)

peso = float(input("Peso:"))
altura = float(input("Altura: "))

imc = peso/(pow(altura,2))

if(imc < 18.5):
    print("ABAIXO DO PESO")
elif(imc < 25):
    print("PESO IDEAL")
elif(imc < 30):
    print("SOBREPESO")
elif(imc < 40):
    print("OBESIDADE")
elif(imc > 40):
    print("OBESIDADE MORBIDA")