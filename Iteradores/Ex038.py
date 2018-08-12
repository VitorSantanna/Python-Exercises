
def isprimo(a):
    x = 1
    z = 0
    while x < a+1:
        y = (a % x == 0)
        if y == 1:
            z = z+1
        x = x+1
    return 1 if z < 3 and a != 1 and a != 0 else 0


for i in range(0, 100):
    if isprimo(i) == 1:
        print(i)
    else:
        continue








