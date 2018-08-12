from funcoes import isprimo

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o ultimo número: "))
for i in range(a, b+1):
    if isprimo(i) == 1:
        print(i)
    else:
        continue



