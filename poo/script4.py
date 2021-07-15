class Prova:
    def __init__(self, data, disciplina, nota):
        self.data = data
        self.disciplina = disciplina
        self.nota = nota


class Aluno:
    def __init__(self, nome, matricula, idade, provas):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.provas = provas
        
    def score(self):
        soma = 0
        quantidade = len(self.provas)
        
        for prova in self.provas:
            soma += prova["nota"]
            
        return soma / quantidade
    
# joao_mat = Prova('14/07/2021', 'Matemática', 7)
# joao_geo = Prova('14/07/2021', 'Geografia', 5)
joao_mat = {
    "data": '14/07/2021',
    "disciplina": 'Matemática',
    "nota": 7
}
joao_geo = {
    "data": '14/07/2021',
    "disciplina": 'Geografia',
    "nota": 5
}
provas_joao = [joao_mat, joao_geo]
joao = Aluno('Joao', 1312, 32, provas_joao)

score_joao = joao.score()

print(score_joao)