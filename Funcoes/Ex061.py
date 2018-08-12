def inverter_ordem(lista):
    lista_invertida=""
    for i in enumerate(lista):
        vetor = (i[0])
        lista_invertida += lista[-vetor-1]



    return(lista_invertida)

def palindromo(texto):
    if inverter_ordem(texto) == texto:
        saida = "Palíndromo"
    else:
        saida = "Não Palíndromo"

    return print(saida)



palindromo("arara")