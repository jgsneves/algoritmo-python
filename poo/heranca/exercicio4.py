class Pessoa:
    def __init__(self, nome, email, data_nascimento) -> None:
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        
class Cliente(Pessoa):
    def __init__(self, nome, email, data_nascimento, relacionamento) -> None:
        super().__init__(nome, email, data_nascimento)
        self.relacionamento = relacionamento
        
class Funcionario(Pessoa):
    def __init__(self, nome, email, data_nascimento, salario) -> None:
        super().__init__(nome, email, data_nascimento)
        self.salario = salario
        
    def aumentarSalario(self):
        self.salario *= 1.10
        
class Administrador(Funcionario):
    def __init__(self, nome, email, data_nascimento, salario) -> None:
        super().__init__(nome, email, data_nascimento, salario)
        
class Gerente(Funcionario):
    def __init__(self, nome, email, data_nascimento, salario) -> None:
        super().__init__(nome, email, data_nascimento, salario)
        
    def aumentarSalario(self):
        self.salario *= 1.20
        
        
joao = Funcionario('joao', 'teste@teste.com', '20', 1000)
maria = Gerente('Maria', 'Testes@fsaudi.com', '32983', 1000)
jose = Administrador('jose', 'teste@este.com', '39213', 1000)

joao.aumentarSalario()
maria.aumentarSalario()
jose.aumentarSalario()

print(joao.salario)
print(maria.salario)
print(jose.salario)