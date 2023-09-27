from os import system as cmd
from time import sleep as wait

def rerrada():
    cmd('cls')
    print('Digites apenas valores correspondentes ao menu.')
    wait(3)
    cmd('cls')

i = 0
clientes = [{"nome": [], 
             "email": []}]
aux = True

while aux:
    #primeiro menu
    print('1 - Cadastrar clientes \n2 - Listar clientes\n3 - Sair')
    a = None
    try :
        a = input('')
    except KeyboardInterrupt :
        pass
    if a == '1' :
        #cadatrar clientes
        cmd('cls')
        print('1 - Cadastrar\n2 - Voltar\n3 - Encerrar')
        try :
            a = input('')
        except KeyboardInterrupt :
            pass
        if a == '1' :
            while True :
                cmd('cls')
                clientes.nome[i] = input('Digite o nome : ')
                clientes.email[i] = input('Digite o email : ')
                cmd('cls')
                i += 1
                break
        elif a == '2' :
            cmd('cls')
            continue
        elif a == '3' :
            aux = False
        else:
            rerrada()
    elif a == '2' :
        #Listar clientes
        cmd('cls')
        print(clientes.nome)
        print(clientes.numero)
    elif a == '3' :
        #sair
        cmd('cls')
        print('Até logo. . .')
        aux = False
    else :
        rerrada()