'''
Faça uma função recursiva chamada printstr() que imprima na tela uma string (caractere a caractere).
'''

def printstr(string):
    if not string:
        return
    print(string[0])
    return printstr(string[1:])

printstr('Suetone')