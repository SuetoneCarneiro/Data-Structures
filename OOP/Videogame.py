from datetime import date

class Videogame:

    cont_numero_serie = 10324 #aleatory

    def __init__(self, marca=None, modelo=None, data_fabricacao=None, capacidadeHD=None, serie=None,jogos=None,garantia=None):
        self.incrementa_contador()
        self.marca = marca
        self.modelo = modelo
        self.data_fabricacao = data_fabricacao if data_fabricacao else date.today()
        self.capacidade = capacidadeHD
        self.serie = self.cont_numero_serie
        self.jogos = jogos
        self.garantia = garantia

        
    def __str__(self) -> str:
        return f'{self.marca}/{self.modelo} - {self.data_fabricacao}'

    @classmethod
    def incrementa_contador(cls):
        cls.cont_numero_serie += 1


vg1 = Videogame(data_fabricacao='2024-02-24', marca='Microsoft', modelo='Xbox One')
vg2 = Videogame(marca='Sony', modelo='PlayStation 2', data_fabricacao='2024-01-02',
                capacidadeHD='100GB', jogos='GTA SAN ANDREAS, BOMBA PATCH FOREVER, MIDNIGHT CLUB 3, GUITAR HERO BRAZUCAS', garantia='Eterna')


print('Video game 1: ', vg1)
print('Video game 2: ', vg2)
