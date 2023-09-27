from os import system as cmd
from time import sleep as wait

def rerrada():
    cmd('cls'), print('Digites apenas valores correspondentes ao menu.'), wait(3), cmd('cls')

i , aux, clientes = 0 , True, {"nome": [], "email": [],"endereco":[]}

while aux:
    cmd('cls')
    print('[1] - Cadastrar clientes\n[2] - Listar clientes\n[3] - Encerrar programa')
    a = None
    try:
        a = input('')
    except KeyboardInterrupt:
        pass

    if a == '1' :
        while True:
            cmd('cls'), print('[1] - Cadastrar\n[2] - Voltar\n[3] - Encerrar')
            try:
                a = input('')
            except KeyboardInterrupt:
                pass
            if a == '1':
                cmd('cls')
                clientes['nome'].append(input('Digite o nome: '))
                clientes['email'].append(input('Digite o email: '))
                clientes['endereco'].append(input('Digite o endereço: '))
                cmd('cls')
                print('Cliente cadastrado com sucesso !')
                wait(3)
                i += 1
            elif a == '2':
                cmd('cls')
                break
            elif a == '3':
                cmd('cls') , print('Encerrando . . .') , wait(3)
                aux = False
            else:
                rerrada()            
    elif a == '2' :
        cmd('cls'), print(f'Você tem {i} clientes cadastrados')
        if i != 0 :
            for x in range(i):
                print(f"Cliente {x+1} Nome: {clientes['nome'][x]}, Email: {clientes['email'][x]}, Endereço: {clientes['endereco'][x]}")
        cmd('pause')
    elif a == '3' :
        cmd('cls'), print('Encerrando . . .'), wait(3)
        aux = False
    else:
        rerrada()