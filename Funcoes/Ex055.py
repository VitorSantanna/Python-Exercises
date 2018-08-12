def fatorial(num):
    fat = num

    for i in range(num, 1, -1):
        if fat==num: #Primeira Execução do For carrega o número do fatorial a ser descoberto
            fat = i*(i-1)
        if i != num: #Demais execuções multiplica o número pelo anterior a fim de descobrir o fatorial.
            fat = fat*(i-1)
    return(print(fat))

fatorial(6)