def infoString(a: str):
    quantidade_de_letras = 0
    espaço = 0
    digito = 0
    alfa = 0
    for i in a:
        if i == ' ':
            espaço += 1
        elif i.isdigit():
            digito += 1
        elif i.isalpha():
            alfa += 1
        elif i == ',':
            alfa += 1

        quantidade_de_letras +=1
    print(f'A string contem {quantidade_de_letras} caracteres, tem {espaço} espaços em branco, {digito} digitos e {alfa} alfabéticos.')


i = 'Thiago Henrique de Azevedo Ribeiro, 26'
print(infoString(i))