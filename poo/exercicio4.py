import abc

class Campeonato(abc.ABC):
    def __init__(self, nome, local, premiacao, patrocinadores):
        self.nome = nome
        self.local = local
        self.premiacao = premiacao
        self.patrocinadores = patrocinadores
        self.inscritos = []
        
    # falta o método de pontuacao
        
    @abc.abstractmethod
    def inscrever_atleta(self, atleta):
        self.inscritos.append(atleta)
        
class Amador(Campeonato):
    def __init__(self, nome, local, premiacao, patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = 'amador'
        
    def inscrever_atleta(self, atleta):
        return super().inscrever_atleta(atleta)

class Profissional(Campeonato):
    def __init__(self, nome, local, premiacao, patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = 'profissional'
        
    def inscrever_atleta(self, atleta):
        if atleta.categoria == 'profissional' or atleta.categoria == 'lenda':
            return super().inscrever_atleta(atleta)
        
class Lenda(Campeonato):
    def __init__(self, nome, local, premiacao, patrocinadores):
        super().__init__(nome, local, premiacao, patrocinadores)
        self.categoria = 'lenda'
        
    def inscrever_atleta(self, atleta):
        if atleta.categoria == 'lenda':
            return super().inscrever_atleta(atleta)
        
class Atleta:
    def __init__(self, nome, idade, pontuacao, categoria):
      self.nome = nome
      self.idade = idade
      self.pontuacao = pontuacao
      self.categoria = categoria
      
camp1 = Campeonato('campeonato teste', 'salvador', None, None)