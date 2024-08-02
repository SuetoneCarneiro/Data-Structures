from array_ifpb import Array

class Fila:

    def __init__(self):
        ...
    
    def enfileirar(self, elemento):
        ...

    def desenfileirar(self):
        ...

    def imprimir(self):
        ...

class FilaFacil(Fila):

    def __init__(self):
        self._dados = []

    def enfileirar(self, elemento):
        self._dados.append(elemento)

    def desenfileirar(self):
        return self._dados.pop(0)

    def imprimir(self):
        print(self._dados)

class FilaCheira(Exception):
    pass

class FilaVazia(Exception):
    pass

class FilaSequencial(Fila):

    def __init__(self, tamanho=10):
        self._tamanho = tamanho
        self._dados = Array(tamanho)
        self._inicio = 0
        self._fim = 0

    @property
    def vazia(self):
        return self._fim == 0
    
    def enfileirar(self, elemento):
        if self._fim == self._tamanho:
            raise FilaCheira()
        self._dados[self._fim] = elemento
        self._fim += 1

    def desenfileirar(self):
        if self.vazia:
            raise FilaVazia()
        valor = self._dados[self._inicio]
        self._inicio += 1
        return valor
    
    def __repr__(self) -> str:
        msg = '['
        for i in range(self._inicio, self._fim):
            e = self._dados[i]
            msg += f'{e}, '
        msg += ']'
        return msg

    def imprimir(self):
        print(self)

class FilaCircular(FilaSequencial):

    def __init__(self, tamanho=10):
        super().__init__(tamanho)
        self._quantidade = 0

    @property
    def fim(self):
        return self.get_posicao(self._fim)
    
    @property
    def inicio(self):
        return self.get_posicao(self._inicio)
    
    def get_posicao(self, n):
        return n % self._tamanho
    
    @property
    def cheia(self):
        return self._quantidade == self._tamanho
    
    def enfileirar(self, elemento):
        if self.cheia:
            raise FilaCheira()
        self._dados[self.get_posicao(self.fim)] = elemento
        self._fim += 1
        self._quantidade += 1

    def desenfileirar(self):
        if self.vazia:
            raise FilaVazia()
        valor = self._dados[self.inicio]
        self._inicio += 1
        self._quantidade -= 1
        return valor
    
    def __repr__(self) -> str:
        msg = '['
        for i in range(self._inicio, self._fim):
            e = self._dados[self.get_posicao(i)]
            if i != self._fim - 1:
                msg += f'{e}, '
            else:
                msg += str(e)
        msg += ']'
        return msg
    

class Node:

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class FilaEncadeada(Fila):
    pass
