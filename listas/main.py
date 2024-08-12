from lista import ListaSimples, ListaSequencial

def teste_lista_simples():
    l = ListaSimples()
    assert len(l) == 0
    assert str(l) == "[]"
    assert l.vazia == True
    l.inserir(0, "abc")
    assert l.obter(0) == "abc"
    assert l[0] == "abc"
    l.remover(0)
    assert l.vazia
    l.inserir(0, 123)
    l.atribuir(0, 456)
    l[0] = 678
    assert l[0] == 678
    print('Lista simples - OK')

def teste_lista_sequencial():
    l = ListaSequencial()
    assert str(l) == "[]"
    assert len(l) == 0
    assert l.vazia
    l.inserir(1000, "abc")
    assert str(l) == "['abc']"
    assert l[0] == "abc"
    l.inserir(100, "def")
    l.inserir(100, "fgh")
    l.inserir(1, "funciona")
    assert l[1] ==  "funciona"
    l.remover(2)
    assert l[2] == "fgh"
    l.remover(2)
    assert len(l) == 2
    assert l[1] == "funciona"
    l.remover(0)
    assert len(l) == 1
    assert l[0] == "funciona"
    print('Lista sequencial - OK')

if __name__ == '__main__':
    teste_lista_simples()
    teste_lista_sequencial()