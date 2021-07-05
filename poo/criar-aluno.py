from nota import Nota
from aluno import Aluno

prova_matematica = Nota('Prova 01', 'Matemática', 9)
prova_historia = Nota('Prova 01', 'História', 7)
prova_geografia = Nota('Prova 01', 'Geografia', 5)

aluno_joao = Aluno('João', 5, 5050)

aluno_joao.adicionar_prova(prova_matematica)
aluno_joao.adicionar_prova(prova_historia)
aluno_joao.adicionar_prova(prova_geografia)

print(aluno_joao.score())