from nota import Nota

class Aluno:
    def __init__(self, nome, semestre, matricula) -> None:
        self.nome = nome
        self.semestre = semestre
        self.matricula = matricula
        self._notas = []
        self._somatorio_notas = 0

    def adicionar_prova(self, nova_prova):
        if (isinstance(nova_prova, Nota)):
            self._notas.append(nova_prova)
        else:
            print('Insira uma nota válida!')

    def score(self):
        if len(self._notas) < 1:
            print('Este aluno não tem nenhuma avaliação!')
        else:
            for nota in self._notas:
                self._somatorio_notas = self._somatorio_notas + nota.valor
                
            quantidade_de_provas = len(self._notas)

            return self._somatorio_notas / quantidade_de_provas