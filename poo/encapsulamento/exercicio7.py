class ContaCorrente:
    def __init__(self, titularNome, banco, agencia, contaCorrente):
        self.__titularNome = titularNome
        self.__banco = banco
        self.__agencia = agencia
        self.__contaCorrente = contaCorrente

    @property
    def titularNome(self):
        return self.__titularNome

    @titularNome.setter
    def titularNome(self, novo_nome):
        self.__titularNome = novo_nome

    @property
    def banco(self):
        return self.__banco

    @banco.setter
    def banco(self, novo_banco):
        self.__banco = novo_banco

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, nova_agencia):
        self.__agencia = nova_agencia

    @property
    def contaCorrente(self):
        return self.__contaCorrente

    @contaCorrente.setter
    def contaCorrente(self, nova_conta):
        self.__contaCorrente = nova_conta