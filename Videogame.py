from datetime import date

seriesNumber = 10454 # aleatory

class Videogame:
    def __init__(self, marca=None, modelo=None, fabricacao=None, capacidadeHD=None, numeroDeSerie=None,jogos=None,garantia=None):
        self.marca = marca
        self.modelo = modelo
        self.fabricacao = fabricacao
        self.capacidade = capacidadeHD
        self.serie = numeroDeSerie
        self.jogos = jogos
        self.garantia = garantia

        global seriesNumber

        if self.fabricacao == None: self.fabricacao = date.today()

        if self.serie == None:
            self.serie = seriesNumber
            seriesNumber += 1
    
    def info(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nData de fabricação: {self.fabricacao}')
        print(f'Capacidade do HD: {self.capacidade}\nNº de série: {self.serie}\nJogos: {self.jogos}')
        print(f'Garantia: {self.garantia}')

def linha():
    print('-'*25)

vg1 = Videogame()
vg2 = Videogame(fabricacao='2024-02-25')
vg3 = Videogame(fabricacao='204-02-24', marca='Microsoft', modelo='Xbox One')
vg4 = Videogame(marca='Sony', modelo='PlayStation 2', fabricacao='2024-01-02',
                capacidadeHD='100GB', jogos='GTA SAN ANDREAS, BOMBA PATCH FOREVER, MIDNIGHT CLUB 3, GUITAR HERO BRAZUCAS', garantia='Eterna')

linha()
print('Video game 1')
vg1.info()
linha()
print('Video game 2')
vg2.info()
linha()
print('Video game 3')
vg3.info()
linha()
print('Video game 4')
vg4.info()
