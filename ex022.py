lista_1 = [[1,2,3],[4,5,6],[7,8,9]] # 45

lista_2 = [[1,2,3],[4,5,6],[7,8,9],['10','11','12']] #78

lista_3 = [[1,2,3],[4,5,6],[7,8,9],['10','11','12'],['A','B','C']] #276

def comString(lista):
    guardar = 0
    a = 0
    for i in lista:
        i = lista[a]
        for n in i:
            if n in i:
                try:
                    n = int(n)
                    guardar += n
                except ValueError:
                    n = ord(n)
                    guardar += n
        a += 1
    return guardar

print(comString(lista_2))