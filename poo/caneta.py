class Caneta:
    def __init__(self, cor, espessura, carga, marca):
        self.cor = cor
        self.espessura = espessura
        self.carga = carga
        self.marca = marca
    

caneta_bic_azul = Caneta('azul', 0.5, 100, 'BIC')

caneta_vermelha_compactor = Caneta('vermelha', 0.5, 100, 'Compactor')

print(caneta_bic_azul)