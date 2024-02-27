from datetime import date

class Videogame:
    def __init__(self, marca=None, modelo=None, fabricacao=None, capacidadeHD=None, numeroDeSerie=None,jogos=None,garantia=None):
        self.marca = marca
        self.modelo = modelo
        self.fabricacao = fabricacao
        self.capacidade = capacidadeHD
        self.serie = numeroDeSerie
        self.jogos = jogos
        self.garantia = garantia
    
        if self.fabricacao == None: self.fabricacao = date.today()
        

vg1 = Videogame(fabricacao="2024-02-25", numeroDeSerie=0)
vg2 = Videogame()
vg3 = Videogame()

print(vg1.serie, vg1.fabricacao)
print(vg2.serie, vg2.fabricacao)
print(vg3.serie, vg3.fabricacao)
