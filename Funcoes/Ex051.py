def encontre_maior(a, b, c):
    if a > b > c or a > c > b:
        print("O número {} é o maior".format(a))
    elif c > a > b or c > b > a:
        print("O número {} é o maior".format(c))
    else:
        print("O número {} é o maior".format(b))


encontre_maior(6, 5, 9)