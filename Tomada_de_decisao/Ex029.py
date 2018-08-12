caracter = str(input("Digite um caracter: ").upper().strip())
if 'A' in caracter or 'E' in caracter or 'I' in caracter or 'O' in caracter or 'U' in caracter:
    print("Vogal")
else:
    print("Consoante")