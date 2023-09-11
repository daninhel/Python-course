import os
#recolhe os dados
num = int(input('Digite um numero para exibir sua taboada: '))
print("=" * 30)

#realiza as operações enquanto o contador for menor que 10 e ja retorna para o usuario
contador = 0
while contador <= 10 :
    print(f"{contador} X {num} = {num * contador}")
    contador += 1

#saida do programa
print("=" * 30)
print(f"Aqui esta a taboada do {num} !")
os.system('pause')
#input('Pressione qualquer tecla para continuar . . .')