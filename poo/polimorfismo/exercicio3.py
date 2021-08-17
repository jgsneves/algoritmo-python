class Animal:
    def __init__(self, peso, patas, porte) -> None:
        self.peso   = peso
        self.patas  = patas
        self.porte  = porte
        
    def locomover(self):
        print('locomovendo...')
        
class Humano(Animal):
    def __init__(self, peso, patas, porte, inteligencia) -> None:
        super().__init__(peso, patas, porte)
        self.inteligencia = inteligencia
        
    def locomover(self):
        print('caminhando....')
        
class Cobra(Animal):
    def __init__(self, peso, porte, veneno) -> None:
        super().__init__(peso, 0, porte)
        self.veneno = veneno
    
    def locomover(self):
        print('rastejando...')
        
        
animal1 = Animal(20, 4, 'medio')


humano1 = Humano(70, 4, 'medio', 50)

cobra1 = Cobra(10, 'pequeno', 50)