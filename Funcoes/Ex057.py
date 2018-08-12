
def contador_de_strings(texto):
    maiusculas = 0
    minusculas = 0
    for i in enumerate(texto):
        if i[1] == str.upper(i[1]):
            maiusculas = maiusculas + 1
        if i[1] == str.lower(i[1]):
            minusculas = minusculas + 1

    return print("Quantidade de caracteres minusculos: ",minusculas,"\nQuantidade de caracteres maiusculos: ",maiusculas)






contador_de_strings("Legendários, o melhor programa.")