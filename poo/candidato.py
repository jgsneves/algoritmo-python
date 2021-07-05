from prova import Prova

class Candidato:
    def __init__(self, nome, endereco, tempo_experiencia, descricao) -> None:
        self.nome = nome
        self.endereco = endereco
        self.tempo_experiencia = tempo_experiencia
        self.descricao = descricao
        self.prova = None

    def adicionar_prova(self, nova_prova):
        if (isinstance(nova_prova, Prova)):
            self.prova = nova_prova
        else:
            print('Insira uma prova válida')

    def isApproved(self):
        if self.prova.pontuacao > 8:
            return True
        else:
            return False