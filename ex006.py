#ex : faça um algoritmo que leia a largura e a altura de uma parede em metros,
#calcule a sua area e a quantidade de tinta necessaria para pinta-la,
#sabendo que cada litro de tinta pinta uma area de 2m^2

#importa bibliotecas e funções
from os import system as cmd
from time import sleep as wait
#coleta os dados
print("=" * 30)
print("Calcule quantas latas de tinta são necessarias para pintar uma parede")
height = float(input("Insira a altura da parede em metros: "))
width = float(input("Insira a largura da parede em metros: "))
#calcula
area = width * height
#calcua quantos baldes gasta de acordo com a area
litros = area / 2
litros = round(litros , 2)

print("Aguarde enquanto fazemos o calculo ;)")
wait(4)
#retona o resultado do calculo para o usuario
cmd('cls')
print("=" * 30)
print(f"Serão necessarios {litros} litros para pintar sua parede cuja a área é de {area} m²")
cmd('pause')
