

def maiorX(X,Y,soma):
    i = 0
    X = X -1
    while(X > Y):
        if(X % 2 != 0):
            soma = soma + X
        X = X -1
    return soma
    

def maiorY(X,Y,soma):
    i = 0
    Y = Y - 1
    while(Y > X):
        if(Y % 2 != 0):
            soma  = soma + Y
        Y = Y - 1
    return soma


X = int(input())
Y = int(input())

soma = 0
if(X > Y):
   soma = maiorX(X,Y,soma)
elif(Y > X):
    soma = maiorY(X,Y,soma)
elif(X == Y):
    soma = 0

print(soma)
