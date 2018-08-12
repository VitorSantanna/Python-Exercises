

x= int(input("Determine o inicio do intervalo:"))
y= int(input("Determine o fim do intervalo:"))
z= int(input("Digite um número: "))


def intervalo(x,y,z):
    if (z > x) and (z < y):
        print("Pertence ao intervalo!")
    else:
        print("Não pertence ao intervalo!")


intervalo(x,y,z)
