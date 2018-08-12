def funcao(x, y):
    x = x+1
    if y:
        x = x+y
    return print(x)


x = int(input("Digite o valor de x: "))
try:
    y = int(input("Digite o valor de y: "))
except:
    y = None


funcao(x, y)