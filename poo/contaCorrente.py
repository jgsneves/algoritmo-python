class ContaCorrente:
    def __init__(self, agencia, numero, senha, titular, banco='01', saldo=0.01) -> None:
        self.agencia = agencia
        self.numero = numero
        self.senha = senha
        self.titular = titular
        self.banco = banco
        self.saldo = saldo