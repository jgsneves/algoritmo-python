class Pessoa:
    def __init__(self, cpf, nome, genero, data_nascimento) -> None:
        self.cpf                = cpf
        self.nome               = nome
        self.genero             = genero
        self.data_nascimento    = data_nascimento
        
        
class Aluno(Pessoa):
    def __init__(self, cpf, nome, genero, data_nascimento, matricula, curso, mensalidade) -> None:
        super().__init__(cpf, nome, genero, data_nascimento)
        self.matricula      = matricula
        self.curso          = curso
        self.mensalidade    = mensalidade
        
    def aumentarMensalidade(self):
        self.mensalidade *= 1.10
        
class Bolsista(Aluno):
    def __init__(self, cpf, nome, genero, data_nascimento, matricula, curso) -> None:
        super().__init__(cpf, nome, genero, data_nascimento, matricula, curso, 0)
        
    def aumentarMensalidade(self):
        self.mensalidade += 100
        
   
joao = Pessoa(31231, 'joao', 'masculino', '938103')
maria = Aluno(894, 'maria', 'fem', '9380193', 389127839, 'direito', 100)
jose = Bolsista(3109238, 'jose', 'mas', 98012, 38091283, 'Direito')