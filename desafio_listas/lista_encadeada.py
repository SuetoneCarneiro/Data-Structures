from array_ifpb import Array

class ListaCheiaExeption(Exception):
    pass


class ListaVaziaException(Exception):
    pass


class Lista:

    @property
    def vazia(self):
        ...

    def __len__(self):
        ...

    def __str__(self):
        ...

    def __repr__(self):
        return str(self)
    
    def imprimir(self):
        return print(self)
    
    def inserir(self, posicao, valor):
	    ...

    def remover(self, posicao):
        ...
    
    def obter(self, posicao):
        ...
         
    def atribuir(self, posicao, valor):
        self._dados[posicao] = valor

    def __getitem__(self, posicao):
        return self.obter(posicao)
    
    def __setitem__(self, posicao, valor):
        self.atribuir(posicao, valor)


class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class ListaEncadeada(Lista):

    def __init__(self):
        self.head: Node | None = None
        self._quantidade = 0

    @property
    def vazia(self):
        return self._quantidade == 0
    
    @property
    def cheia(self):
        return False
    
    def __len__(self):
        return self._quantidade
    
    def _get_no_indice(self, posicao):
        if posicao >= len(self):
            raise IndexError()
        no = self.head
        for i in range(posicao):
            no = no.proximo
        return no
    
    def get_antecessor(self, posicao):
        return self._get_no_indice(posicao - 1)
    
    def inserir(self, posicao, valor):
        posicao = self._get_posicao(posicao)
        novo = Node(valor)
        if self.vazia:
            self.head = novo
        elif posicao == 0:
            novo.proximo = self.head
            self.head = novo
        elif posicao > self._quantidade:
            antecessor = self.get_antecessor(self._quantidade)
            novo.proximo = antecessor.proximo
            antecessor.proximo = novo
        else:
            antecessor = self.get_antecessor(posicao)
            novo.proximo = antecessor.proximo
            antecessor.proximo = novo

        self._quantidade += 1

    def remover(self, posicao):
        posicao = self._get_posicao(posicao)
        if self.vazia:
            raise ListaVaziaException()

        if posicao == 0:
            self.head = self.head.proximo
        else:
            antecessor = self.get_antecessor(posicao)
            antecessor.proximo = antecessor.proximo.proximo

        self._quantidade -= 1

    def __str__(self):
        s = '['
        no = self.head
        for i in range(self._quantidade):
            s += repr(no.valor)
            if i < self._quantidade - 1:
                s += ', '
            no = no.proximo
        s += ']'
        return s
    

    def _get_posicao(self, posicao):
        if posicao < 0:
            return len(self) - posicao
        return posicao

    def obter(self, posicao):
        posicao = self._get_posicao(posicao)
        no = self._get_no_indice(posicao)
        return no.valor

    def atribuir(self, posicao, valor):
        posicao = self._get_posicao(posicao)
        no = self._get_no_indice(posicao)
        no.valor = valor

    # QUESTÃO 1 -----------------------
    def intersecao(lista1, lista2):
        new_list = ListaEncadeada()
        for i in range(len(lista1)):
            if lista1.obter(i) in lista2:
                new_list.inserir(100, lista1.obter(i))

        return new_list

    def uniao(lista1, lista2):
        new_list = ListaEncadeada()
        for i in range(len(lista1)):
            if lista1.obter(i) not in new_list:
                new_list.inserir(100, lista1.obter(i))
            if lista2.obter(i) not in new_list:
                new_list.inserir(100, lista2.obter(i))
            
        return new_list

    def diferenca(lista1, lista2):
        new_list = ListaEncadeada()
        for i in range(len(lista1)):
            if lista1.obter(i) not in lista2:
                new_list.inserir(100, lista1.obter(i))

        return new_list
    
    # QUESTÃO 2 -----------------------------
    def remover_duplicidades(self):
        ...         

    # QUESTÃO 3 -----------------------------
    def maiores_que(self, valor):
        new_list = ListaEncadeada()
        for i in range(len(self)):
            if self.obter(i) > valor:
                new_list.inserir(1000, self.obter(i))
        
        return new_list

    #QUESTÃO 4 ------------------------------
    def map(self, func):
        new_list = ListaEncadeada()
        for element in self:
            new_list.inserir(100, func(element))
        
        return new_list
