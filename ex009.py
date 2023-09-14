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
if len(letra) > 1 or letra.isalpha() == False :
    print("FALEI PRA INSIRIR APENAS UMA LETRA")
else:
    vogais = ['a','e','i','o','u']
    letra = letra.lower()
    #condição para conferir se é vogal
    if letra in vogais:
        print("é uma vogal")
    else:
        print("é consoante")

cmd('pause')