def removedor(*numeros):
    lista = []
    for i in numeros:
        if i not in lista:
            lista.append(i)


    return print(lista)


lista = 1, 2, 3, 3, 3, 3, 4, 5
removedor(*lista)

