from os import system as cmd
from time import sleep as wait

#menu de inicio
message = "Digite uma letra para saber se é vogal ou consoante"

print("=" * len(message))
print(message)
print("=" * len(message))
wait(4)
cmd('cls')
#coleta de dados
letra = input('Insira UMA letra: ')
#verifica se é letra e apenas uma letra
if len(letra) > 1 or letra.isdigit() == True :
    print("FALEI PRA INSIRIR APENAS UMA LETRA")
else:
    vogais = ['a','e','i','o','u']
    letra = letra.lower() #converte para letra minuscula
    if letra in vogais: #condição para conferir se é vogal
        print("é uma vogal")
    else:
        print("é consoante")

cmd('pause')