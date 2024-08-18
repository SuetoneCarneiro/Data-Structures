from array_ifpb import Array

class Pilha:
    def __init__(self):
        ...

    def empilhar(self, elemento):
        ...

    def desempilhar(self):
        ...

    def imprimir(self):
        ...

    @property
    def topo(self):
        ...
    
class PilhaVazia(Exception):
    pass

class PilhaCheia(Exception):
    pass

class PilhaExeption(Exception):
    pass


class Node:

    def __init__(self, valor, proximo: 'Node' = None):
        self.valor = valor
        self.proximo = proximo
    

class PilhaEncadeada:
    
    def __init__(self):
        self._topo: None|Node = None
        self._tamanho = 0

    @property
    def tamanho(self):
        return self._tamanho
    
    @property
    def vazia(self):
        return self.tamanho == 0
    
    def empilhar(self, elemento):
        self._topo = Node(elemento, proximo=self._topo)
        self._tamanho += 1

    def desempilhar(self):
        if self.vazia:
            raise PilhaVazia()
        
        self._topo = self._topo.proximo
        self._tamanho -= 1

    def imprimir(self):
        atual: Node = self._topo
        while atual:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()

    def desempilha_n( self, n): 
        '''
        Operação para remoção de n elementos a partir do topo da pilha.
        Argumentos:
        int n: o número de elementos que se deseja desempilhar a partir do topo da
        pilha
        Retorno:
        True : Se os n elementos foram desempilhados
        False: Não foi possível desempilhar a quantidade n de elementos.
        '''
        for i in range(n):
            if self.vazia:
                return False
            self._topo = self._topo.proximo
            self._tamanho -= 1
        return True

    def esvazia(self):
        '''while not self.vazia:
            self.desempilhar'''
        self.desempilha_n(self.tamanho)

    def obtemBase(self):
        '''
        Devolve o conteúdo armazenado na base da pilha
        Retorno:
        int valor - O conteúdo armazenado na base da pilha
        Exceção:
        PilhaException(): Quando a pilha não tiver elemento na base
        '''
        if self.vazia:
            raise PilhaExeption()
        atual = self._topo
        while atual.proximo != None:
            atual = atual.proximo
        return atual.valor
    
    def obtem(self, pos):
        if pos > self._tamanho:
            raise IndexError()
        atual = self._topo
        for _ in range(pos):
            atual = atual.proximo
        return atual.valor

    @property
    def subTopo(self):
        '''
        Operação para obtenção do conteúdo armazenado no subtopo da pilha.
        Retorno: o conteúdo armazenado no subtopo da pilha
        Exceções: PilhaExeption(), quando a pilha não tiver subtopo
        '''
        if self.vazia or self._topo.proximo == None:
            raise PilhaExeption('Não há subtopo')
        return self._topo.proximo.valor

    @property
    def topo(self):
        if self.vazia:
            raise PilhaVazia()
        return self._topo.valor


def teste1():
    print('-------- TESTE 1 --------')
    print('SubTopo')
    p = PilhaEncadeada()
    p.empilhar("1")
    assert p.topo == "1"
    p.empilhar("2")
    print('Pilha: ', end=' ')
    p.empilhar("3")
    p.imprimir()
    print('Subtopo: ',p.subTopo)

def teste2():
    print('-------- TESTE 2 --------')
    print('Desempilha N')
    p = PilhaEncadeada()
    for i in range(7):
        p.empilhar(i)
    p.imprimir()
    print('Retorno da função:',p.desempilha_n(4),'\nDesempilhando 4 elementos...')
    p.imprimir()

def teste3():
    print('-------- TESTE 3 --------')
    print('Esvazia')
    p = PilhaEncadeada()
    for i in range(7):
        p.empilhar(i)
    p.imprimir()
    print('Esvaziando...')
    p.esvazia()
    p.imprimir()
    print('Pilha vazia')

def teste4():
    print('-------- TESTE 4 --------')
    print('Obtem Base')
    p = PilhaEncadeada()
    for i in range(5):
        p.empilhar(i)
    p.imprimir()
    print('base:', p.obtemBase())


if __name__ == "__main__":
    teste1()
    teste2()
    teste3()
    teste4()
