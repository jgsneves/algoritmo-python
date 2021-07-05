class Funcionario:
    def __init__(self, nome, cpf, salario) -> None:
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        
    def aumento_anual_salario(self):
        self.salario = self.salario * 1.15
        
    
        
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados) -> None:
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qtd_gerenciados = qtd_gerenciados
        
    def aumento_anual_salario(self):
        self.salario = self.salario * 1.30
        
        
operador_joao = Funcionario('João', 12313, 2000)
operador_joao.aumento_anual_salario()

gerente_jose = Gerente('José', 974321371, 5000, 123456, 2)
gerente_jose.aumento_anual_salario()

print(operador_joao.salario)
print(gerente_jose.salario)
