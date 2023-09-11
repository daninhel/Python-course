from os import system as cmd
from time import sleep as wait

#menu de inicio
message = "Digite um valor para saber se é par ou impar"

print("=" * len(message))
print(message)
print("=" * len(message))
wait(4)
cmd('cls')
#armazena o numero em uma variavel
numero = float(input("digite um numero: "))
#verifica se o numero é par ou impar
if numero%2 == 1 :
    print('o numero é impar')
else:
    print('o numero é par')
#encerra o sistema
cmd('pause')