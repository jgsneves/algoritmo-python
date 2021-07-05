class Medico:
    def __init__(self, crm, nome, idade, salario) -> None:
        self.crm = crm
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def ehAposentado(self):
        if self.idade > 55:
            return True
        else:
            return False
        
    def valorAposentadoria(self):
        return self.salario * 0.8
        
class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario) -> None:
        super().__init__(crm, nome, idade, salario)
    
    def ehAposentado(self):
        if self.idade >= 50:
            return True
        else:
            return False
        
    def valorAposentadoria(self):
        return super().valorAposentadoria() + 2000
    
class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario) -> None:
        super().__init__(crm, nome, idade, salario)
        
    def ehAposentado(self):
        if self.idade >= 60:
            return True
        else:
            return False
 
medico_paulo = Medico(1010, 'Paulo', 45, 12000)

print('Paulo é aposentado? ', medico_paulo.ehAposentado())
print('Valor da pensão de paulo: ', medico_paulo.valorAposentadoria())
        
cirurgiao_jose = Cirurgiao(2020, 'José', 56, 15000)

print('José é aposentado? ', cirurgiao_jose.ehAposentado())
print('Valor da pensão de José: ', cirurgiao_jose.valorAposentadoria())

auxiliar_joao = Auxiliar(5050, 'João', 56, 10000)

print('João é aposentado? ', auxiliar_joao.ehAposentado())
print('Valor da pensão de João: ', auxiliar_joao.valorAposentadoria())