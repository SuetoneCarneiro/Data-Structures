'''
Dado um vetor de números inteiro, escreva uma função recursiva para identificar o maior valor
armazenado no vetor.
'''

maior = 0
def greaterElement(vector):
    global maior
    if vector == []:
        return maior
    
    if vector[0] > maior:
        maior = vector[0]
    
    return greaterElement(vector[1:])

print(greaterElement([2, 55, 6, 99, 45, 12, 9]))
