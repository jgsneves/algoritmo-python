from candidato import Candidato
from prova import Prova
from processoSeletivo import ProcessoSeletivo

candidato_joao = Candidato('Joao', 'Rua de Baixo', 3, 'Dev frontend')
prova_joao = Prova('05/07', 9)
candidato_joao.adicionar_prova(prova_joao)

candidato_pedro = Candidato('Pedro', 'Rua de Cima', 2, 'Dev backend')
prova_pedro = Prova('05/07', 6)
candidato_pedro.adicionar_prova(prova_pedro)

candidato_roberta = Candidato('Roberta', 'Rua do Meio', 6, 'Dev fullstack')
prova_roberta = Prova('05/07', 9)
candidato_roberta.adicionar_prova(prova_roberta)

processo_seletivo_junho = ProcessoSeletivo()

processo_seletivo_junho.inscritos.append(candidato_pedro)
processo_seletivo_junho.inscritos.append(candidato_joao)
processo_seletivo_junho.inscritos.append(candidato_roberta)

aprovados = processo_seletivo_junho.getApprovedList()

print(aprovados)