from time import sleep as wait
from os import system as cmd

clientes, aux = [], True

def verificacao(a: bool) -> bool:
    '''
    verifica se há clientes, caso não haja o parametro ira receber falso e diz que não é possivel.
    '''
    if not clientes:
        cmd('cls'), print('Não é possivel pois não há clientes cadastrados'), wait(3), cmd('cls')
        a = False
    else:
        a = True
    return a
def create(nome: str , telefone: str , email: str, idade: int) -> list:
    '''
    Adiciona clientes na lista.
    '''
    clientes.append([nome,telefone,email,idade])
    wait(2), print('Cliente cadastrado com sucesso !'), wait(2), cmd('cls')
def read() -> None:
    for i in range(0,len(clientes)):
        print(f'Cliente {i + 1}\n   nome: {clientes[i][0]}, telefone: {clientes[i][1]}, email: {clientes[i][2]}, idade: {clientes[i][3]} .')
def update(index: int, nome: str , telefone: str , email: str, idade: int) -> None:
    '''
    Altera os dados do cliente (que é passado pelo index)
    '''
    clientes[index][0] = nome
    clientes[index][1] = telefone
    clientes[index][2] = email
    clientes[index][3] = idade
    cmd('cls'), print('Atualizado com sucesso !'), wait(2), cmd('cls')
def delete(index: int) -> None:
    '''
    Recebe o index do cliente que sera deletado e o deleta conforme o index
    '''
    del clientes[index - 1]
    cmd('cls'), print('Cliente deletado com sucesso !'), wait(2), cmd('cls')

while aux:
    msg = 'Cadastro de clientes'
    print(len(msg) * '='), print(msg), print(len(msg) * '=')
    del msg

    print(f'Você tem {len(clientes)} cadastrados\n1 - Cadastrar cliente\n2 - Ver clientes cadastrados\n3 - Alterar cadastros\n4 - Deletar algum cadastro\n5 - Encerrar programa')
    
    a = None
    try:
        a = input('Digite o numero que corresponde a opção desejada: ')
        cmd('cls')
    except KeyboardInterrupt:
        pass

    if a == '1':
        while True:
            print(f'Você tem {len(clientes)} cadastrados\n1 - Cadastrar cliente\n2 - Voltar para o menu principal\n3 - Encerrar o programa')
            
            try:
                a = input('Digite o numero que corresponde a opção desejada: ')
                cmd('cls')
            except KeyboardInterrupt:
                pass
            
            if a == '1':
                try:
                    nome = input('Insira o nome do cliente: ').capitalize()
                    telefone = input('insira o telefone do cliente: ')
                    email = input('insira o email do cliente: ')
                    idade = None
                    try:
                        idade = int(input('insira a idade do cliente: '))
                    except ValueError:
                        print('Insira apenas valores válidos')
                    create(nome, telefone, email, idade)
                    del nome, telefone, email, idade
                except KeyboardInterrupt:
                    print('Insira apenas valores válidos')
            elif a == '2':
                break
            elif a == '3':
                aux = False
                break
            else:
                continue
    elif a == '2':
        while True:
            a = None
            a = verificacao(a)
            if a:
                read(), cmd('pause'), cmd('cls')
                break
            else:
                break
    elif a == '3':
        a = verificacao(a)
        if a:
            while True:
                print('Digite o numero de qual cliente voce pretende atualizar.')
                read()
                try:
                    index = int(input('Numero do cliente que você pretende atualizar: ')) - 1
                    nome = input('Digite o novo nome: ').capitalize()
                    telefone = input('Digite o novo telefone: ')
                    email = input('Digite o novo email: ')
                    idade = int(input('Digite a nova idade: '))
                    update(index, nome , telefone, email, idade)
                except:
                    print('Digite apenas dados validos.')
                
                try:
                    a = input('Se deseja atualizar mais clientes digite 1, caso não deseja aperte qualquer tecla.')    
                except KeyboardInterrupt:
                    pass
                
                if a == '1':
                    a = verificacao(a)
                    if a :
                        continue
                    else:
                        break
                else:
                    break
        else:
            continue
    elif a == '4':
            a = verificacao(a)
            if a:
                while True:
                    read()
                    a = None # index
                    try:
                        a = input('Digite o numero que corresponde ao cliente que você deseja remover: ')
                        try:
                            a = int(a)
                        except ValueError:
                            print('Insira apenas valores válidos')
                    except KeyboardInterrupt:
                        print('Digite apenas valores válidos')
                    delete(a)
                    try:
                        a = input('Deseja deletar mais algum  cliente?\nDigite 1 caso deseje,e qualquer outra tecla para  voltar ao menu principal.').lower()
                    except KeyboardInterrupt:
                        pass
                    
                    if a == '1':
                        verificacao(a)
                        if a :
                            continue
                        else:
                            break
                    else:
                        break
            else:
                continue
    elif a == '5':
        aux = False
print('Programa encerrado . . .')
