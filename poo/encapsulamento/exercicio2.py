class Carro:
    def __init__(self, marca, modelo, cor, ligado, velocidadeAtual):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = ligado
        self.velocidadeAtual = velocidadeAtual
        self.vidaUtilBuzina = 10000

    def ligar(self):
        if (self.ligado):
            print('O carro já está ligado!')
        else:
            self.ligado = True

    def desligar(self):
        if (self.ligado):
            self.ligado = False
        else:
            print('O carro já está desligado!')

    def buzinar(self):
        if (self.vidaUtilBuzina):
            print('Bibi!')
            self.vidaUtilBuzina -= 1
        else:
            print('A buzina chegou ao seu fim de vida. Não foi possível buzinar')
    def acelerar(self):
        if self.ligado and self.velocidadeAtual <= 110:
            self.velocidadeAtual += 10
        else:
            print('Impossível acelerar. Ou o carro está desligado ou chegou em sua velocidade máxima')
    
    def desacelerar(self):
        if self.ligado and self.velocidadeAtual >= 10:
            self.velocidadeAtual -= 10
        else:
            print('Impossível acelerar. Ou o carro está desligado ou chegou em sua velocidade mínima.')
            