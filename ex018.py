from os import system as cmd

numero = int(input('Digite um numero para saber seu fatorial: '))

if numero == 0:
    numero = 1
else:
    for i in range(0,numero-1):
        numero += numero * i

cmd('cls')
print(f'O fatorial do numero digitado é {numero}.')