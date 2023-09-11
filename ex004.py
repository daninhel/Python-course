from cmath import sqrt
#da as instruções para realizar o calculo
print(30*'=')
print('Calcula equação de 2 grau')
print(30*'=')
print("siga o formato da equação genêrica e insira os elementos na ordem")
print("a . x² ± b . x ± c = 0")
print('OBS: só iremos dar os resultados se fizer parte dos reais e inteiros')
print(30*'=')
#coleta as informações
a = int(input("Coloque o relativo à termo 'a' : "))
b = int(input("Coloque o relativo à termo 'b' : "))
c = int(input("Coloque o relativo à termo 'c' : "))
#eraliza o calculo do delta
delta = (b**2) - 4 * a * c
raiz_delta = sqrt(delta)
#verifica o resultado de delta e realiza a formula de bhaskara
if delta < 0 :
   print("Seu resutlado não existe dentro dos reais")
else :
    #realiza a conta de x um e x dois
    x_primeiro = (-(b)+raiz_delta)/(2 * a)
    x_segundo = (-(b)-raiz_delta)/(2 * a)
    #deixa apenas duas casas decimais
    x_primeiro = round(x_primeiro, 2)
    x_segundo = round(x_segundo, 2)
    #exibe o resutlado para o usuario
    print(f" seu x 1º é {x_primeiro} e seu x 2º é {x_segundo}")
    
input('Pressione qualquer tecla para continuar. . .')

#5x^2 -3x + 8 = 0 