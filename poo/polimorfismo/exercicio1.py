class Medico:
    def __init__(self, crm, nome, idade, salario) -> None:
        self.crm = crm
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def aposentar(self):
        if self.idade >= 55:
            self.salario *= 0.8
        else:
            print("este médico não tem idade para se aposentar!")
            
class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario) -> None:
        super().__init__(crm, nome, idade, salario)
        
    def aposentar(self):
        if self.idade >= 50:
            self.salario += 2000
        else:
            print("este médico não tem idade para se aposentar!")

class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario) -> None:
        super().__init__(crm, nome, idade, salario)
        
    def aposentar(self):
        if self.idade >= 60:
            self.salario *= 0.7
        else:
            print("este médico não tem idade para se aposentar!")