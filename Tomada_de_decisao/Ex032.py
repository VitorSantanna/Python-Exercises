data = input("Digite uma data: ").strip()

try:
    if data[0:1].isnumeric() and data[2] == '/' and data[3:4].isnumeric() and data[5] == '/' and data[6:9].isnumeric():
      print("Data válida")
except:
     print("Data inválida!")
     

