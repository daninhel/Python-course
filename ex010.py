from os import system as cmd
from time import sleep as wait

#coleta os dados
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kilogramas: "))
cmd('cls')
print('Calculando . . .')
wait(5)
cmd('cls')
#verifica
categoria = ""
if peso < 65 :
    categoria = "pena"
elif peso >= 65 and peso < 72 :
    categoria = "leve"
elif peso >= 72 and peso < 79 :
    categoria = "ligeiro"
elif peso >= 79 and peso < 86 :
    categoria = "meio-médio"
elif peso >= 86 and peso < 93 :
    categoria = "médio"
elif peso >= 93 and peso < 100 :
    categoria = "meio-pesado"
elif peso < 100 :
    categoria = "pesado"
#retorna
print(f"Olá, {nome.capitalize()}! seu peso é {peso}kg e você se encontra na categoria {categoria.capitalize()}.")
cmd('pause')