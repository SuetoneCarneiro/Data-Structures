'''
Implemente uma função recursiva que converta um número da base decimal para qualquer uma das
seguintes bases: binária (2), octal (8) e hexadecimal (16). A função deve obedecer ao seguinte protótipo: 

def decToBase(num, base)
'''

def decToBase(num, base):
    if num // base == 0:
        return 1
    return str(decToBase(num//base, base)) + str(num%base) 

print(decToBase(100, 2))
print(decToBase(100, 8))
print(decToBase(16, 16)) # nao funciona para todos os casos
