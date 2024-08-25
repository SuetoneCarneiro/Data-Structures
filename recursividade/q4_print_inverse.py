'''
Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário
'''

def printInverse(string):
    if not string:
        return
    print(string[-1])
    return printInverse(string[:-1])

printInverse('Estruturas')