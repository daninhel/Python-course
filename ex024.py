import csv
import time
import datetime
from os import system as cmd

id = 1
tarefas : []

    

def add():
    tarefas = []
    cmd('cls')
    nome = input("Passe o nome da tarefa : ")
    data = datetime.date.today().strftime('%d/%m/%Y')
    hora = datetime.datetime.now().strftime('%H:%M:%S')
    tarefa = {
        'id' : len(tarefas) + 1,
        'data' : data,
        'hora' : hora,
        'nome' : nome
    }
    
    tarefas.append(tarefa)
    
    with open('todo.csv', 'a') as todo:
        for coisa in tarefa:
            todo.write(coisa)

def read():
    cmd('cls')
    with open('todo.csv', 'r') as todo:
        todo = todo.readlines()
        for lista in todo:
            print(lista.replace('\n',''))
        cmd('pause')

def menu():
    print('To-do List\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Encerrar')
    op = input()
    return op
    
def main():
    cmd('cls')
    op = menu()
    match op:
        case '1':
            add(),main()
        case '2':
            read(),main()
        case '3':
            ...
        case _:
            print('Opção inválida'),time.sleep(3),main()

if __name__ == '__main__':
    main()