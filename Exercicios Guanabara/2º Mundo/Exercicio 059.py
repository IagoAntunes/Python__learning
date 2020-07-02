
#Crie um programa que leia dois valores e mostre um menu na tela:# [ 1 ] somar
#[ 2 ] multiplicar  [ 3 ] maior  [ 4 ] novos números  [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input("Numero1: "))
n2 = int(input("Numero2:"))
opcao=0
while(opcao != 5):
    opcao = int(input("\n[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos Numeros \n[5]Sair"))

    if (opcao == 1):
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    elif(opcao == 2):
        mult = n1 * n2
        print(f"{n1} * {n2} = {mult}")
    elif(opcao == 3):
        maior = n1
        if(n2 > maior):
            maior = n2
        print(f"Maior Numero é {maior}")
    elif(opcao == 4):
        n1 = int(input("Numero1: "))
        n2 = int(input("Numero2:"))
    elif(opcao == 5):
        print("Obrigado,Volte Sempre")
        exit(0)