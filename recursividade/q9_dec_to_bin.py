'''
Faça uma função recursiva chamada decToBin() que receba um número inteiro na base decimal e
imprima seu correspondente na base binária. O protótipo da função é definido por: def decToBin( num )
'''

def decToBin(num):
    if num // 2 == 0:
        return 1
    return str(decToBin(num//2)) + str(num%2) 

print(decToBin(100))
