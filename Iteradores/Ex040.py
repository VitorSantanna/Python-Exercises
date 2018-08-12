a = int(input("Escreva o primeiro número: "))
b = int(input("Escreva o ultimo número: "))
c = int(input("Defina o primeiro número a ser descartado: "))
d = int(input("Defina o segundo número a ser descartado: "))
e = int(input("Defina o terceiro número a ser descartado: "))
for i in range(a, b):
    if i == c or i == d or i == e:
        continue
    print(i)