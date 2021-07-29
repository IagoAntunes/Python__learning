
n1 = int(input("Largura: "))
n2 = int(input("Altura: "))


while(n2 > 0):
    count = n1
    while(count > 0):
        print("#", end="")
        count = count - 1
    print()
    n2 = n2 - 1
