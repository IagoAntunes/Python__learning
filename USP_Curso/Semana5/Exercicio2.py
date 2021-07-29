

def éPrimo(n1):
    count = 0
    i = 1
    while(i <= n1):
        if(n1 % i == 0):
            count = count + 1
        i = i + 1
    if(count == 2):
        return 1

def maior_Primo(x):
    achou = 1
    if(1 == éPrimo(x)):
        return x
    while(achou != 0):
        x = x -1
        if(éPrimo(x)==1):
            achou = 1
            return x
        
n1 = int(input("Numero 1: "))

print(maior_Primo(n1))