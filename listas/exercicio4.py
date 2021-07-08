notas = {}
nome_aluno = ''

def calcular_media_aluno(nome):
    acc = float()
    for nota in notas[nome]:
        acc += nota
    quantidade = len(notas[nome])
    return acc / quantidade

while not nome_aluno:
    nome_aluno = input('Digite o nome do aluno: ')
    nota_1 = float(input('Digite a primeira nota do aluno: '))
    nota_2 = float(input('Digite a segunda nota do aluno: '))
    notas[nome_aluno] = [nota_1, nota_2]
    pergunta_media = input('Deseja saber a média deste aluno? (s/n) ')
    if pergunta_media == 's':
        print(calcular_media_aluno(nome_aluno))
    pergunta_fim = input('Deseja continuar o programa? (s/n) ')
    if pergunta_fim == 'n':
        continuar_programa = False
    
print(notas)