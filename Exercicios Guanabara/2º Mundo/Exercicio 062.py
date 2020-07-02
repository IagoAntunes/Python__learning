
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
opcao = 1
while(opcao != 0):
    num = int(input("Numero:"))
    fat = 1
    i = num
    while(i != 0):
        fat = fat * i
        i = i -1
    print(f"FATORIAL = {fat}")
    opcao = int(input("Deseja Continuar ?"))