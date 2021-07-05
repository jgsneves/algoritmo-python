class Instrumento:
    def __init__(self, nome, grau_dificuldade, professor) -> None:
        self.nome = nome
        self.professor = professor
        self.grau_dificuldade = grau_dificuldade
        
    def dificuldade(self):
        return self.grau_dificuldade - self.professor.pontuacao
        
class Professor:
    def __init__(self, nome, pontuacao) -> None:
        self.nome = nome
        self.pontuacao = pontuacao

class Corda(Instrumento):
    def __init__(self, nome, grau_dificuldade, professor, qtd_corda, tipo_corda) -> None:
        super().__init__(nome, grau_dificuldade, professor)
        self.qtd_corda = qtd_corda
        self.tipo_corda = tipo_corda
        
    def dificuldade(self):
        if self.tipo_corda == 'aço':
            return (self.grau_dificuldade - self.professor.pontuacao)*self.qtd_corda
        else:
            super().dificuldade()
        
class Percussao(Instrumento):
    def __init__(self, nome, grau_dificuldade, professor, baqueta) -> None:
        super().__init__(nome, grau_dificuldade, professor)
        self.baqueta = baqueta
        
    def dificuldade(self):
        if self.baqueta:
            return super().dificuldade() + 5
        else:
            return super().dificuldade()
        
professor_jose = Professor('José', 7)

violao = Corda('Violão', 4, professor_jose, 4, 'aço')
flauta = Instrumento('Flauta', 6, professor_jose)

print(violao.dificuldade())
print(flauta.dificuldade())