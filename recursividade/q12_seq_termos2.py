'''
Faça uma função recursiva denominada seqTermos2() que calcule a soma dos n termos da série:
2/4 + 5/5 + 10/6 + 17/7 + ... + (n^2 + 1)/(n+3)
'''

def seqTermos2(n):
    if n == 1:
        return 1/2
    return (n**2 + 1)/(n+3) + seqTermos2(n-1)

print(seqTermos2(3))