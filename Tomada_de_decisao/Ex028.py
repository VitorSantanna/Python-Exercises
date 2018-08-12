n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

if n1 >= n2 and n2 >= n3:
    print("{}, {}, {}".format(n3, n2, n1)) #Possibilidades 3*3 = 9. Possibilidade 1: O N1 é o maior dos valores seguido do n2
elif n2 >= n1 and n1 >= n3:
    print("{}, {}, {}".format(n3, n1, n2)) #Possiblidade 2: o N2 é o maior dos valores seguidos do n1
elif n3 >= n1 and n1 >= n2:
    print("{}, {}, {}".format(n2, n1, n3))#Possiblidade 3: o N3 é o maior dos valores seguidos do n1
elif n3 >= n2 and n2 >= n1:
    print("{}, {}, {}".format(n1, n2, n3))#Possiblidade 4: o N3 é o maior dos valores seguidos do n2
elif n1 >= n2 and n3 >= n2:
    print("{}, {}, {}".format(n2, n3, n1))#Possiblidade 5: o N1 é o maior dos valores seguidos do n3
elif n2 >= n3 and n3 >= n1:
    print("{}, {}, {}".format(n1, n3, n2))#Possiblidade 6: o N2 é o maior dos valores seguidos do n3
elif n2 >= n3 and n3 >= n1:
    print("{}, {}, {}".format(n1, n2, n3))#Possiblidade 7: o N1 é o maior dos valores seguidos do n3

