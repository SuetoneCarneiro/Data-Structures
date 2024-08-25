'''
Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma
seria igual a 1 + 2 + 3 = 6
'''

def soma_n(n):
    if n == 0:
        return n
    return n + soma_n(n-1)

print(soma_n(3))