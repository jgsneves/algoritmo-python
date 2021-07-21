class Aluno:
    def __init__(self, nome, sobrenome, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self.__sobrenome = novo_sobrenome

    @property
    def matricula(self):
        return self.__matricula
