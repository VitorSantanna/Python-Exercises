import funcoes

def numero_primo(*lista):
    lista_primo = []
    for i in lista:
        if funcoes.isprimo(i):
            lista_primo.append(i)

    return  print(lista_primo)




numero_primo(1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)

