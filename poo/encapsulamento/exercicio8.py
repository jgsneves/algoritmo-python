class Funcionario:
    def __init__(self, nome, salario, matricula, funcao):
        self.nome = nome
        self.__salario = salario
        self.__matricula = matricula
        self.funcao = funcao

    @property
    def matricula(self):
        return self.__matricula

    @property
    def salario(self):
        return 'R$ {0:.2f}'.format(self.__salario)

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario == self.__salario * 1.20:
            self.__salario = novo_salario
        else:
            print('Só é possível dar aumentos de 20%. Não é possível diminuir o salário.')
