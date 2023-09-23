from time import sleep as wait
from os import system as cmd

while True:
    print("Digite 1 para iniciar. \nOu qualquer tecla para sair do programa.")
    a = None
    try:
        a = input()#capitura a saida do usuario
    except KeyboardInterrupt:
        pass
    #saber qual o valor o usaurio digitou
    if a == '1' :
        cmd('cls')
        tempo = 0
        segundos = 0
        minutos = 0
        while True:
            try:
                tempo += 1
                minutos = tempo // 60
                segundos = tempo % 60
                print(f"Digite CTRL + C para pausar.\nMinutos : {minutos} Segundos : {segundos}")
                wait(1)
                cmd('cls')
            except KeyboardInterrupt :
                cmd('cls')
                print('Cronometro pausado.\nPrecione qualquer tecla para voltar . . .\n1 - Reiniciar\n2 - Sair')
                try :
                    a = input()
                except KeyboardInterrupt:
                    pass
                if a == '1' :
                    cmd('cls')
                    minutos = 0
                    tempo= 0
                    minutos = 0
                    continue
                elif a == '2' :
                    cmd('cls')
                    break
                else :
                    cmd('cls')
                    pass
    else:
        cmd('cls')
        print('Até mais. . .')
        break