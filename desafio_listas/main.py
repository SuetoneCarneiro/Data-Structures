from lista_encadeada import ListaEncadeada

def teste_lista_encadeada():
    l1 = ListaEncadeada()
    l2 = ListaEncadeada()

    # exemplo de conjuntos em: https://mundoeducacao.uol.com.br/matematica/operacao-com-conjuntos.htm
    l1.inserir(100, 1)
    l1.inserir(100, 3)
    l1.inserir(100, 6)
    l1.inserir(100, 9)
    l1.inserir(100, 12)
    l1.inserir(100, 15)
    l1.inserir(100, 18)
    l2.inserir(100, 1)
    l2.inserir(100, 2)
    l2.inserir(100, 4)
    l2.inserir(100, 6)
    l2.inserir(100, 8)
    l2.inserir(100, 10)
    l2.inserir(10, 12)
    l2.inserir(10, 16)

    intersecao = ListaEncadeada.intersecao(l1,l2)
    uniao = ListaEncadeada.uniao(l1, l2)
    diferenca = ListaEncadeada.diferenca(l1, l2)

    print(f'Lista 1: {l1}')
    print(f'Lista 2: {l2}')
    print('-'*50)
    print(f'Interseção: {intersecao}')
    print(f'União: {uniao}')
    print(f'Diferença: {diferenca}')
'''
def teste_duplicidades():
    lista = ListaEncadeada()
    lista.inserir(100, 1)
    lista.inserir(100, 2)
    lista.inserir(100, 3)
    lista.inserir(100, 1)
    lista.inserir(100, 4)
    lista.inserir(100, 5)
    lista.inserir(100, 3)
    lista.inserir(100, 4)

    print(lista)
    lista.remover_duplicidades()
    print(lista)
'''
def teste_maiores_que():
    lista = ListaEncadeada()
    lista.inserir(100, 1)
    lista.inserir(100, 2)
    lista.inserir(100, 3)
    lista.inserir(100, 4)
    lista.inserir(100, 5)
    lista.inserir(100, 6)

    print('Maiores que 3:', lista.maiores_que(3))
    print('Maiores que 5:', lista.maiores_que(5))

def teste_map():

    def quadrado(num):
        return num**2
    
    def mais_10(num):
        return num + 10
    
    lista = ListaEncadeada()
    lista.inserir(100, 1)
    lista.inserir(100, 2)
    lista.inserir(100, 3)
    lista.inserir(100, 4)
    lista.inserir(100, 5)
    lista.inserir(100, 6)
    

    print(lista.map(quadrado))
    print(lista.map(mais_10))


if __name__ == '__main__':
    teste_lista_encadeada()
    #print('*'*50)
    #teste_duplicidades()
    print('*'*50)
    teste_maiores_que()
    print('*'*50)
    teste_map()
