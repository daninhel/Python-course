from time import sleep as wait
from os import system as cmd
clientes = []

def verificacao():
    '''
    verifica se há clientes, caso não haja o parametro ira receber falso e diz que não é possivel.
    '''
    if not clientes:
        cmd('cls'), print('Não é possivel pois não há clientes cadastrados'), wait(3), cmd('cls')
        a = False
    else:
        a = True
    return a

def create():
    '''
    Adiciona clientes na lista.
    '''
    try:
        nome = input('Insira o nome do cliente: ').capitalize()
        telefone = input('insira o telefone do cliente: ')
        email = input('insira o email do cliente: ')
        idade = None
        try:
            idade = int(input('insira a idade do cliente: '))
        except ValueError:
            print('Insira apenas valores válidos')
    except KeyboardInterrupt:
        print('Insira apenas valores válidos')
    return [nome, telefone, email, idade]

def read():
    for i in range(0,len(clientes)):
        print(f'Cliente {i + 1}\n   nome: {clientes[i][0]}, telefone: {clientes[i][1]}, email: {clientes[i][2]}, idade: {clientes[i][3]} .')

def update():
    '''
    Altera os dados do cliente (que é passado pelo index)
    '''
    read()
    index = receive('menu1')
    try:
        index = int(index) - 1
        clientes[index][0] = input('Digite o novo nome: ')
        clientes[index][1] = input('Digite o novo telefone: ')
        clientes[index][2] = input('Digite o novo email: ')
        try:
            clientes[index][3] = int(input('Digite a nova idade: '))
        except ValueError :
            print('Digite apenas valores validos.')
    except KeyboardInterrupt:
            print('Digite apenas valores validos.')
    cmd('cls'), print('Atualizado com sucesso !'), wait(2), cmd('cls')

def setDelete():
    '''
    Recebe o index do cliente que sera deletado e o deleta conforme o index
    '''
    read()
    index = receive('menu1')
    if index.isdigit():
        del clientes[int(index) - 1]
        cmd('cls'), print('Cliente deletado com sucesso !'), wait(2), cmd('cls')
    else:
        print('Digite apenas números que correspondem ao menu.'), wait(3)

def receive() -> str :
    '''
    Recebe os inputs e já trata casos de Keyboard Interrupt.
    '''
    if a == 'menu1':
        try:
            a = input('Digite o numero que corresponde a opção desejada: ')
            cmd('cls')
        except KeyboardInterrupt:
            cmd("cls")
            pass
    if a == 'menu2':
        try: #menu2
            a = input('Se deseja realizar esta ação novamente digite 1, caso não deseja aperte qualquer tecla.')
        except KeyboardInterrupt:
            cmd('cls')
            pass

    return a

def search() -> None :
    '''
    recebe um nome como string, verifica se ele esta na lista e imprime todas as informações do respectivo nome
    '''
    name = None
    try:
        name = input('Digite o nome do cliente que gostaria de buscar os dados: ')
        p = 0
        for i in clientes:
            cliente = clientes[p]
            if name in cliente:
                print(f'Cliente {p + 1}\n   nome: {cliente[0]}, telefone: {cliente[1]}, email: {cliente[2]}, idade: {cliente[3]} .')
            p += 1
    except KeyboardInterrupt:
        print('Não foi possivel realizar essa ação !')

def menu() -> None:
    '''
    Exibe o menu.
    '''
    cmd('cls'), print(f'Você tem {len(clientes)} cadastrados\n1 - Cadastrar cliente\n2 - Ver clientes cadastrados\n3 - Buscar cliente\n4 - Alterar cadastros\n5 - Deletar algum cadastro\n6 - Encerrar programa')

    a = receive('menu1')
    return a

def main():
    op = menu()

    match op :
        case '1':            
            cliente = create()
            clientes.append(cliente)
            del cliente
            main()
        case '2':
            a = verificacao()
            if a :
                read()
                cmd('pause')
            main()
        case '3':
            a = verificacao()
            if a :
                search()
                cmd('pause')
        case '4':
            a = verificacao()
            if a:
                update()
            main()
        case '5':
            a = verificacao()
            if a :
                setDelete()
            main()
        case '6':
            print('Encerrando . . .')
        case _:
            print('opção invalida')
            main()

if __name__ == '__main__':
    main()