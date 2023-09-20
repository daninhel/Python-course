from os import system as cmd
from time import sleep as wait
from getpass import getpass as password

def responsividade() :
    wait(3)
    cmd('cls')

i = 3
senha = ''

while i != 0 :
    senha_u = password(prompt='Digite sua senha para poder acessar o sistema: ')
    print('Aguarde,verificando senha . . .')
    responsividade()
    if senha_u == senha :
        print("Senha correta, bem-vindo(a) ao sistema !")
        break
    elif i == 0 :
        print("Você atingiu o número máximo de tentativas pertimidas,tente mais tarde.")
        break
    else:
        i -= 1
        print(f"Senhra incorreta, você possui apenas mais {i} tentativas.")
        responsividade()
        continue
cmd('pause')