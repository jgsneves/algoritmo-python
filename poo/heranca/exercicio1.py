class Lutador:
    def __init__(self, nome, altura, categoria):
        self.nome = nome
        self.altura = altura
        self.categoria = categoria
        self.__vitorias = 0
        self.__derrotas = 0
        
    @property
    def vitoria(self):
        return self.__vitorias
    
    def adicionarVitoria(self):
        self.__vitorias += 1
        
    @property
    def derrota(self):
        return self.__derrotas
    
    def adicionarDerrota(self):
        self.__derrotas += 1
        
    def cardLutador(self):
        print('{} tem o card: {} - {}'.format(self.nome, self.vitoria, self.derrota))
        
class Evento:
    def __init__(self, desafiador, desafiado, data):
        self.desafiador = desafiador
        self.desafiado = desafiado
        self.data = data
        self.vencedor = ''
        self.perdedor = ''
        self.realizado = False

    def finalizarEvento(self, vencedor, perdedor):
        self.realizado = True
        self.vencedor = vencedor.nome
        self.perdedor = perdedor.nome
        
        vencedor.adicionarVitoria()
        perdedor.adicionarDerrota()
    
        
    
anderson_silva = Lutador('Anderson silva', 180, 'medio')
minotauro = Lutador('Minotauro', 170, 'medio')

ufc140 = Evento(minotauro, anderson_silva, '04/08/2021')


ufc140.finalizarEvento(anderson_silva, minotauro)

anderson_silva.cardLutador()
minotauro.cardLutador()