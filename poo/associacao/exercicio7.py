class Prova:
    def __init__(self, id, disciplina, nota):
        self.id = id
        self.disciplina = disciplina
        self.nota = nota

class Aluno:
    def __init__(self, nome, semestre, matricula, provas):
        self.nome = nome
        self.semestre = semestre
        self.__matricula = matricula
        self.__provas = provas
        
    def provas(self, nova_prova):
        self.__provas.append(nova_prova)
        
    @property
    def matricula(self):
        return self.__matricula
    
    def aprovar(self):
        self.semestre += 1
        
    def score(self):
        montante_notas = 0
        quantidade = len(self.__provas)
        
        for prova in self.__provas:
            montante_notas += prova.nota
            
        return montante_notas / quantidade
            
prova1 = Prova(1, 'Mat', 7)
prova2 = Prova(2, 'Mat', 5)
prova3 = Prova(3, 'Geo', 8)

joao = Aluno('João', 3, 4040, [])
joao.provas(prova1)
joao.provas(prova2)
joao.provas(prova3)

print(joao.score())