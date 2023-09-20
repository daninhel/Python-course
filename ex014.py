from os import system as cmd
from time import sleep as wait
def reponsividade() :
    wait(3)
    cmd('cls')
    print('Processando . . .')
    wait(4)
    cmd('cls')
def imprimir() :
    print(f'Nome do cliente {i}: {nome}')
    print(f'Idade do cliente {i}: {idade}')
    print(f'Email do cliente {i}: {email}')
while True:
    qnt = input('Digite o número de usuários que deseja cadastrar : ')
    i = 1
    try :
        qnt = int(qnt)
    except ValueError:
        print('Digite apenas números.')
        continue
    while i < qnt + 1 :
        nome = input(f'Digite o nome do cliente {i} : ').capitalize()
        idade = input(f'Digite o idade do cliente {i} : ')
        email = input(f'Digite o email do cliente {i} : ')
        try:
            idade = int(idade)
        except ValueError :
            print('Tente novamente e passe um valor valido')
            continue
        
        i += 1
        reponsividade()
        imprimir()
        reponsividade()
    print("Fim do castro !")
    break
cmd('pause')