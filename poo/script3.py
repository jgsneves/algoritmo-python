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
            soma = soma + prova["nota"]
            
        return soma / quantidade
            
prova_mat = {
    "data": "14/07",
    "disciplina": "Matemática",
    "nota": 7
}

prova_geo = {
    "data": "14/07",
    "disciplina": "Geografia",
    "nota": 5
}

prova_his = {
    "data": "14/07",
    "disciplina": "História",
    "nota": 4
}

provas_de_joao = [prova_mat, prova_geo, prova_his]

joao = Aluno('Joao', 3123, 32, provas_de_joao)

score_de_joao = joao.score()

print(score_de_joao)