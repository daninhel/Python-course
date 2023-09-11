#coleta de dados
print(20 * '=')
print('Calculadora de IMC')
print(20 * '=')
nome = input("Insira seu nome: ").capitalize()
peso = float(input("Insira seu peso em kg (kilogramas): "))
altura = float(input("Insira sua altura em m (metros): "))
#conta para verificar o imc
imc = peso / altura**2
#compara para saber o nivel de imc do usuario
clasf = ''
if imc < 18.5:
    clasf = "abaixo do peso"
elif 18.5 <= imc <= 24.9:
    clasf = "peso normal"
else:
    clasf = "acima do peso"
#retorna os dados para o usuario
print(20 * '=')
print(f"Olá {nome}, seu IMC é {imc: ,.2f} e você se encontra {clasf}.")
input("Pressione qualquer tecla para continuar . . .")