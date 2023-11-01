import requests
import csv
from os import system as cmd

from time import sleep as wait

api = "https://apiaulas.thiagodev502.repl.co/funcionarios"
cabecario = ['ID','Nome', 'Cargo', "Salario"]

def WriteCsv(dados:list):
    with open('api.csv', 'w') as arquivo:
        escrever = csv.writer(arquivo, delimiter=',')
        escrever.writerow(cabecario)
        for dicionario in dados:
            id, nome, cargo, salario = dicionario['id'], dicionario['nome'], dicionario['cargo'], dicionario['salario']

            lista = [id,nome,cargo,salario]
            escrever.writerow(lista)

while True:
    try:
        cmd('cls')
        print('Pressione Ctrl + C para parar o programa.')
        dados = requests.get(api).json()
        WriteCsv(dados)
    except KeyboardInterrupt:
        break
    print('Atualizado com sucesso !')
    wait(30)