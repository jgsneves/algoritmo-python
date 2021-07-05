from nota import Nota

class Aluno:
    _notas = []

    def __init__(self, nome, semestre, matricula) -> None:
        self.nome = nome
        self.semestre = semestre
        self.matricula = matricula

    def adicionar_prova(self, nova_prova):
        if (isinstance(nova_prova, Nota)):
            self._notas.append(nova_prova)
        else:
            print('Insira uma nota válida!')

    def score(self):
        somatorio_notas = 0

        for nota in self._notas:
            somatorio_notas = somatorio_notas + nota.valor
            
        quantidade_de_provas = len(self._notas)

        return somatorio_notas / quantidade_de_provas