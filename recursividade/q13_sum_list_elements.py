'''
Dado um vetor de números reais, escreva uma função recursiva para determinar a soma dos elementos
do vetor.
'''

def sumListElements(list):
    if list == []:
        return 0
    return list[0] + sumListElements(list[1:])

print(sumListElements([1,2,3,4,5,6,7,8,9,10]))
