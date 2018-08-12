d = int(input("Informe a quantidade de dias: "))
h = int(input("Informe a quantidade de horas: "))
m = int(input("Informe a quantidade de minutos: "))
s = int(input("Informe a quantidade de segundos: "))

dtos = ((d*24) * 60) * 60
htos = (h*60) * 60
mtos = m*60
totals= dtos + htos + mtos + s
print("O total de segundos é: {}".format(totals))
