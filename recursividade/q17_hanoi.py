'''
Torre de Hanói é um "quebra-cabeça" clássico com solução via recursividade que consiste em uma base
contendo três pinos, em um dos quais são dispostos alguns discos uns sobre os outros, em ordem
crescente de diâmetro, de cima para baixo. O problema consiste em passar todos os discos de um pino
para outro qualquer, usando um dos pinos como auxiliar, de maneira que um disco maior nunca fique em
cima de outro menor em nenhuma situação. O número de discos pode variar sendo que o mais simples
contém apenas três.

É interessante observar que o número mínimo de "movimentos" para conseguir transferir todos os discos
da primeira estaca à terceira é 2n-1, sendo n o número de discos. Logo:
 >> Para solucionar um Hanói de 4 discos, são necessários 15 movimentos
 >> Para solucionar um Hanói de 7 discos, são necessários 127 movimentos
 >> Para solucionar um Hanói de 15 discos, são necessários 32.767 movimentos

Acompanhe a solução recursiva do problema da Torre de Hanói e exiba o que vai ser impresso na tela.
'''

def moveTower(numDiscos,origem, destino, auxiliar):
    '''
    numDiscos: int - Quantidade de discos a movimentar.
    origem: identificador da torre de origem
    destino: identificador da torre destino.
    temp: identificador da torre auxiliar
    '''
    if numDiscos >= 1:
        moveTower(numDiscos-1,origem,auxiliar,destino)
        moveDisco(origem,destino)
        moveTower(numDiscos-1,auxiliar,destino,origem)

def moveDisco(origem,destino):
    print("Movendo disco da haste",origem,"para a haste",destino)
    
moveTower(3,"A","B","C")
