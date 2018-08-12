""" Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros
 que estejam associados a uma chave.
 Em seguida, imprima na tela o nome da chave e o respectivo valor:"""

def argumentos_biblioteca(*a):
    print(a)


a = {"A": "B", 1: 'C'}
argumentos_biblioteca(a)

