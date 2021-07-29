
num = int(input("Digite um Numero: "))

i = num-1
if(num == 0):
    print("1")
else:
    while(i != 0):
        num = num * i
        i = i - 1
    print(num)

