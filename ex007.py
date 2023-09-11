from os import system as cmd
from time import sleep as wait

message = "Calculo de média"

print(len(message) * "=")
print(message)
print(len(message) * "=")
wait(3)
cmd('cls')

#coleta os dados
print('Utilize a escala de 0 a 100')
nome = input("Digite o nome do aluno: ")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a  terceira nota: "))
nota4 = int(input("Insira a quarta nota: "))
cmd('cls')
#calcula os dados
print('Arguarde alguns segundos . . .')
wait(3)

media = (nota1+nota2+nota3+nota4)/4
#verificação
if media > 50 :
    situação = 'aprovado'
else: 
    situação = 'reprovado'
#retorna os resultados dos calculos para o usuário
print(f"A situação do aluno {nome} é {situação} pois sua média foi de {media}.")