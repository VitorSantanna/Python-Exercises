o = int(input("Digite o primeiro octeto do seu ip: "))
if o > 0 and o <= 127:
    print("A classe do seu ip é 'A'")
if o >= 128 and o <= 191:
    print("A classe do seu ip é 'B'")
if o >=192 and o <= 223:
    print("A classe do seu ip é 'C'")
if o >= 224 and o <= 239:
    print("A classe do seu ip é 'D'")
if o > 240:
    print("A classe do seu ip é 'E'")
