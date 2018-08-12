def removedor(*numeros):
    lista = []
    for i in numeros:
        if i % 2 == 0:
            lista.append(i)


    return print(lista)


lista = 1, 2, 3, 3, 3, 3, 4, 5, 6
removedor(*lista)
