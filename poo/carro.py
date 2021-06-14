class Carro:
    def __init__(self, marca, modelo, ano, velocidade, ligado, automatico) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico

    def ligar(self):
        if self.ligado == False:
            self.ligado = True
            print('Ligando o carro...')
        else:
            print('O carro já está ligado!')
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print('Desligando o carro...')
        else:
            print('O carro já está desligado!')

    def acelerar(self, velocidade):
        if self.ligado == True:
            if velocidade <= 120:
                self.velocidade = velocidade
                print('Velocidade atual: {}'.format(self.velocidade))
            else:
                print('O carro tem uma velocidade máxima de 120km/h.')
        else:
            print('O carro está desligado. Antes de acelerar devemos liga-lo.')

    def verificarMarcha(self):
        if self.velocidade < 20:
            print('O carro encontra-se na marcha 1.')
        elif self.velocidade == 20:
            print('O carro encontra-se na marcha 2.')
        elif self.velocidade >= 30 and self.velocidade <= 35:
            print('O carro encontra-se na marcha 3.')
        elif self.velocidade >= 45 and self.velocidade <= 50:
            print('O carro encontra-se na marcha 4.')
        elif self.velocidade >= 60:
            print('O carro encontra-se na marcha 5.')
        else:
            print('O carro não está engrenado.')