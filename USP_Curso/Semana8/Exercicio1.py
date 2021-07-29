
def remove_repetidos(lista,lists2):
    j = 0
    for i in range(0,len(lista)):
        while(j < len(lista2)):
            if(lista[i] == lista[j]):
                del lista2[j]
            j = j + 1


lista = [2, 4, 2, 2, 3, 3, 1]
lista2 = lista[:]
remove_repetidos(lista,lista2)
lista2.sort()



                
