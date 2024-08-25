'''
Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores
numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor
inferior a key. O protótipo da função é definido por: def menores_rec( lista, key )
'''
cont = 0
def menores_rec(lista, key):
    global cont
    if lista == []:
        return cont
    
    if lista[0] < key:
        cont += 1

    return menores_rec(lista[1:], key)
    
print(menores_rec([1,2,3], 3))
