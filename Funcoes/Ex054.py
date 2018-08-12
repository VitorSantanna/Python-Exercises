#Versão 1 Invertedor de Ordem
""" def inverter_ordem(lista):
   lista_invertida= lista[-1]
   lista_invertida += lista[-2]
   lista_invertida += lista[-3]
   lista_invertida += lista[-4]
   lista_invertida += lista[-5]
   lista_invertida += lista[-6]
   lista_invertida += lista[-7]
   lista_invertida += lista[-8]
   print(lista_invertida)



lista = "1234abcd"
inverter_ordem(lista)

"""
#Versao 2 Invertor de Ordem
def inverter_ordem(lista):
    lista_invertida=""
    for i in enumerate(lista):
        vetor = (i[0]) # vetor inicial = 0[0] == D
        lista_invertida += lista[-vetor-1] #inverter a posição de D o mandando para o campo -1 da lista, depois -2, -3



    print(lista_invertida)


lista = input("Digite um nome: ")
inverter_ordem(lista)