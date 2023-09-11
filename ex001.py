from datetime import date
#Coleta os dados
print(20 * "=")
print("Cadastro de Clientes")
print(20 * "=")
name = input("Insira seu nome: ").capitalize()
lastName = input("Insira seu sobrenome: ").capitalize()
age = int(input("Insira sua idade: "))
email = input("Insira seu email: ").lower()

#tratar os dados
#ano de nascimento:
current_year =  date.today()
current_year = current_year.year
birth_year = current_year - age
#verificação de idade:
verification = True

if age >= 18 :
    verification = True
else :
    verification = False

#exibe os dados
print(20 * "=")
print(f"Nome completo : {name} {lastName} ")
print(f"Idade : {age} anos")
print(f"Nascido em : {birth_year}")
print(f"Maior de idade ? {verification}")
# print(f"Maior de idade ? {idade>=18}")
input("Pressione qualquer tecla para continuar:")
