'''
Dado um vetor de números inteiro, escreva uma função recursiva para verificar se um vetor está ordenado
ou não.
'''

def isSorted(vector):
    if len(vector) == 1:
        return True

    if vector[0] < vector[1]:
        return isSorted(vector[1:])
    else:
        return False

print(isSorted([1,2,3,4]))
print(isSorted([2,5,4,6]))
print(isSorted([4,5]))
print(isSorted([5,4]))
