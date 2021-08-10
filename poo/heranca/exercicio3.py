class Carro:
    def __init__(self, cor, chassi, velocidade, ligado) -> None:
        self.cor = cor
        self.chassi = chassi
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

class Retro(Carro):
    def __init__(self, cor, chassi, velocidade, ligado, qtdCarburador) -> None:
        super().__init__(cor, chassi, velocidade, ligado)
        self.qtdCarburador = qtdCarburador
        
    def consumir_10_carb(self):
        if self.qtdCarburador >= 10:
            self.qtdCarburador -= 10
        else:
            print('Não há quantidade suficiente!')

class Sporting(Carro):
    def __init__(self, cor, chassi, velocidade, ligado, qtoNitro) -> None:
        super().__init__(cor, chassi, velocidade, ligado)
        self.qtoNitro = qtoNitro
        
    def consumi_10_nitro(self):
        if self.qtoNitro >= 10:
            self.qtoNitro -= 10
        else:
            print('Não há quantidade suficiente!')

class Passeio(Carro):
    def __init__(self, cor, chassi, velocidade, ligado, qtoAC) -> None:
        super().__init__(cor, chassi, velocidade, ligado)
        self.qtoAC = qtoAC

    def consumir_10_AC(self):
        if self.qtoAC >= 10:
            self.qtoAC -= 10
        else:
            print('Não há quantidade suficiente!')