from os import system as cmd
from time import sleep as wait

def responsividade() :
    wait(3)
    cmd('cls')

message = "Quiz"

print("=" * len(message))
print(message)
print("=" * len(message))
responsividade()

contador = 0
respostas_c = ['A','A','A','C','C']
alternativas = [ 'A','B','C','D','E']

#pergunta 1
print("Pergunta 1:")
print("Qual é a capital da França?")
print("A) Paris") #certa
print("B) Berlim")
print("C) Londres")
print("D) Roma")
resposta = input("Digite a letra correspondente à resposta: ")

if resposta.capitalize() == respostas_c[0] :
    print('Correto!')
    contador += 1
else:
    print(f'Errado, a resposta correta é {respostas_c[0]} !')

responsividade()

# Pergunta 2
print("Pergunta 2:")
print("Qual é o maior planeta do nosso sistema solar?")
print("A) Júpiter") #certa
print("B) Terra")
print("C) Saturno")
print("D) Marte")
resposta = input("Digite a letra correspondente à resposta: ")
if resposta.capitalize() == respostas_c[1] :
    print('Correto!')
    contador += 1
else:
    print(f'Errado, a resposta correta é {respostas_c[1]} !')

responsividade()

# Pergunta 3
print("Pergunta 3:")
print("Qual é o número atômico do hidrogênio?")
print("A) 1") #certa
print("B) 2")
print("C) 3")
print("D) 4")
resposta = input("Digite a letra correspondente à resposta: ")
if resposta.capitalize() == respostas_c[2] :
    print('Correto!')
    contador += 1
else:
    print(f'Errado, a resposta correta é {respostas_c[2]} !')

responsividade()

# Pergunta 4
print("Pergunta 4:")
print("Quem pintou a Mona Lisa?")
print("A) Vincent van Gogh")
print("B) Pablo Picasso")
print("C) Leonardo da Vinci") #certa
print("D) Michelangelo")
resposta = input("Digite a letra correspondente à resposta: ")
if resposta.capitalize() == respostas_c[3] :
    print('Correto!')
    contador += 1
else:
    print(f'Errado, a resposta correta é {respostas_c[3]} !')

responsividade()

# Pergunta 5
print("Pergunta 5:")
print("Quantos elementos químicos existem na tabela periódica?")
print("A) 92")
print("B) 108")
print("C) 118") #certa
print("D) 130")
resposta = input("Digite a letra correspondente à resposta: ")
if resposta.capitalize() == respostas_c[4] :
    print('Correto!')
    contador += 1
else:
    print(f'Errado, a resposta correta é {respostas_c[4]} !')

responsividade()

print(f'Sua pontuação foi de {contador} !')
cmd('pause')