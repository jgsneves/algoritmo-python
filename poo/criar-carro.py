from carro import Carro

fusca = Carro('volks', 'fusca', '1970', 0, False, False)

fusca.ligar()

fusca.ligar()

fusca.acelerar(32)
fusca.verificarMarcha()

fusca.acelerar(130)
print('velocidade atual:', fusca.velocidade)

fusca.desligar()