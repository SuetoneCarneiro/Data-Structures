'''
Faça uma função recursiva chamada recursiveLength() que retorne a quantidade de caracteres de um
string.
'''
cont = 0
def recursiveLength(string):
    global cont
    if not string:
        return cont
    cont += 1
    return recursiveLength(string[1:])

print(recursiveLength('abc'))
