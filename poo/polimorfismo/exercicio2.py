
class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__sobrenome = sobrenome
        
    @property
    def getName(self):
        return self.__nome
    
    def retornarIdade(self):
        return self.__idade
    
class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, matricula, curso, mensalidade) -> None:
        super().__init__(nome, sobrenome, idade)
        self.__matricula = matricula
        self.__curso = curso
        self.__mensalidade = mensalidade
        
    def retornarIdade():
        
        
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, idade, salario, descricao) -> None:
        super().__init__(nome, sobrenome, idade)
        self.__salario = salario
        self.__descricao = descricao
        
    def demitir(self):
        print('{} está demitido!'.format(self.getName))
    
    @property
    def salario(self):
        return self.__salario
    
    def aumentarSalario(self):
        self.__salario *= 1.10
        
class Materia:
    def __init__(self, nome, duracao) -> None:
        self.__nome = nome
        self.__duracao = duracao
        
    @property
    def nome(self):
        return self.__nome
        
class Professor(Funcionario):
    def __init__(self, nome, sobrenome, idade, salario, descricao, competencias) -> None:
        super().__init__(nome, sobrenome, idade, salario, descricao)
        self.__competencias = competencias
        self.__listaDeMaterias = []
        
    @property
    def materias(self):
        return self.__listaDeMaterias
    
    def alocarEmMateria(self, materia):
        self.__listaDeMaterias.append(materia)
        
class Coordenador(Funcionario):
    def __init__(self, nome, sobrenome, idade, salario, descricao) -> None:
        super().__init__(nome, sobrenome, idade, salario, descricao)        

    def aumentarSalario(self):
        self.salario *= 1.20
