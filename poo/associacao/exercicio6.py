class Funcionario:
    def __init__(self, id, nome, idade, salario):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
class FolhaDeSalario:
    def __init__(self, funcionarios):
        self.funcionarios = funcionarios
        
    def admitir(self, novo_funcionario):
        self.funcionarios.append(novo_funcionario)
        
    def demitir(self, id):
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                self.funcionarios.remove(funcionario)
                break
            
    def custoComPessoal(self):
        acc = 0
        for funcionario in self.funcionarios:
            acc += funcionario.salario
        return acc
        
joao = Funcionario(1, 'João', 32, 1000)
maria = Funcionario(2, 'Maria', 22, 1000)
jose = Funcionario(3, 'jose', 31, 1000)

folha_mc_donalds = FolhaDeSalario([])
folha_mc_donalds.admitir(joao)
folha_mc_donalds.admitir(maria)
folha_mc_donalds.admitir(jose)

print(folha_mc_donalds.custoComPessoal())