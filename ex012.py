from os import system as cmd

verifica = False

while not verifica :
    #recolhe os dados
    num = input('Digite um numero para exibir sua taboada: ')
    contador = input('Digite até qual número você quer a taboada do numero anterior: ')
    cmd('cls')
    if num.isdigit() and contador.isdigit() :
        auxiliar = 0
        verifica = True
        while auxiliar <= int(contador) :
            auxiliar += 1
            print(f"{auxiliar} X {int(num)} = {int(num) * auxiliar}")
    else :
            verifica = False
#saida do programa
cmd('pause')