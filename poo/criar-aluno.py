from nota import Nota
from aluno import Aluno

prova_matematica = Nota('Prova 01', 'Matemática', 9)
prova_historia = Nota('Prova 01', 'História', 7)
prova_geografia = Nota('Prova 01', 'Geografia', 5)
prova_algebra = Nota('Av 01', 'Álgebra', 2)

aluno_joao = Aluno('João', 5, 5050)
aluno_paulo = Aluno('Paulo', 1, 5051)

aluno_joao.adicionar_prova(prova_matematica)
aluno_joao.adicionar_prova(prova_historia)
aluno_joao.adicionar_prova(prova_geografia)
aluno_joao.adicionar_prova(prova_algebra)

print(aluno_paulo.score())
print(aluno_joao.score())