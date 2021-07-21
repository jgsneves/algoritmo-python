class Aluno:
    def __init__(self, nome, sobrenome, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__matricula = matricula

# observe que o atributo matrícula está inacessível.