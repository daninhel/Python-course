#entrada de dados
capital = int(input('Insira um valor: '))
taxa = float(input('Insira a porcentagem: '))
tempo = int(input('Insira o tempo: '))
#calcular dados
#fomula de juros // juros = capital x taxa x tempo
juros = capital * (taxa/100) * tempo
#formula de montante //  montante = capital inicial + juros
montante = float(capital + juros)
#exibir dados para ususario
print(f"o lucro é de R${juros} e o total investido é de R${montante}")