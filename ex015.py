from time import sleep as wait
from os import system as cmd

while True:
    print("1 - Iniciar")
    print("2 - Sair")
    a = input() #capitura a saida do usuario
    #saber qual o valor o usaurio digitou
    try:
        a = int(a)
    except ValueError:
        print('Digite apenas valores correspondentes ao do menu.')
        continue

    if a == 1 :
        segundos = 0
        minutos = 0
        while True:
            wait(1)
            segundos += 1
            if segundos == 60 :
                minutos += 1
                segundos = 0
            print(f"Minutos : {minutos} Segundos : {segundos}")
            cmd('cls')
    elif a == 2 :
        print('Até mais . . .')
        break
    else:
        print('Digite apenas valores correspondentes ao do menu.')

cmd('pause')