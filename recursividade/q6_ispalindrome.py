'''
Faça uma função recursiva chamada ispalindrome() que retorne verdadeiro caso uma string seja
palíndrome, ou falso caso contrário. O protótipo da operação é definido por: def ispalindrome(str)
'''

res = True
def ispalindrome(str):
    global res
    if not str:
        return res
    if str[0] != str[-1]:
        res = False
    return ispalindrome(str[1:-2])

print(ispalindrome('leel'))
