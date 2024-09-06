class NodeNotFound(Exception):
    ...

class Node:

    def __init__(self, valor):
        self.valor = valor
        self.filho_esquerda: Node | None = None
        self.filho_direita: Node | None = None

    def __repr__(self):
        return f'No(valor={self.valor})'
    
    def add_esquerda(self, valor):
        if self.filho_esquerda is None:
            self.filho_esquerda = Node(valor)

    def add_direitra(self, valor):
        if self.filho_direita is None:
            self.filho_direita = Node(valor)

    @property
    def tem_filho_esquerda(self) -> bool:
        return bool(self.filho_esquerda)

    @property
    def tem_filho_direita(self) -> bool:
        return bool(self.filho_esquerda)

    @property
    def eh_folha(self) -> bool:
        return not self.tem_filho_direita and not self.tem_filho_esquerda
    
class Arvore:
    
    def __init__(self):
        self.raiz: Node | None = None

    @property
    def vazia(self) -> bool:
        return self.raiz is None
    
    def add(self, valor):
        self.raiz = self._add(self.raiz, valor)

    def _add(self, no: Node | None, valor):
        if no is None:
            return Node(valor)
        
        if valor > no.valor:
            no.filho_direita = self._add(no.filho_direita, valor)
        else:
            no.filho_esquerda = self._add(no.filho_esquerda, valor)
        return no
    
    def print(self):
        if not self.vazia:
            self._print_pre_ordem(self.raiz)
        
    def _print_pre_ordem(self, no: Node | None): # raiz -> esquerda -> direita
        if no is None:
            return
        print(no.valor)
        self._print_pre_ordem(no.filho_esquerda)
        self._print_pre_ordem(no.filho_direita)

    def _print_em_ordem(self, no: Node | None): # Esquerda -> raiz -> direita
        if no is None:
            return 
        self._print_em_ordem(no.filho_esquerda)
        print(no.valor)
        self._print_em_ordem(no.filho_direita)

    def _print_pos_ordem(self, no: Node | None): # Esquerda -> direita -> raiz
        if no is None:
            return
        self._print_pos_ordem(no.filho_esquerda)
        self._print_pos_ordem(no.filho_direita)
        print(no.valor)

    def busca(self, valor) -> bool:
        return self._busca(self.raiz, valor)

    def _busca(self, no: Node | None, valor) -> bool:
        if no in None: 
            return False
        elif no.valor == valor:
            return True
        elif valor > no.valor:
            return self._busca(no.filho_direita, valor)
        else:
            return self._busca(no.filho_esquerda, valor)

