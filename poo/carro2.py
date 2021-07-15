class Carro:
    def __init__(self, marca, modelo, cor, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade
        
    def acelerar(self):
        self.velocidade += 10
        
    def desacelerar(self):
        self.velocidade -= 10