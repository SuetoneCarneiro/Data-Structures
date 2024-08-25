'''
Faça uma função recursiva chamada invertString() que retornte a sequência de caracteres de uma
string passada como argumento na ordem inversa
'''

def invertString(string):
    if string == '':
        return ''
    return string[-1] + invertString(string[:-1])

print(invertString('good morning'))