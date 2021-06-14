sistema_acabou = False
notas = 0
quantidade_de_notas = 0

while not sistema_acabou:
    notas += float(input('Digite a nota do aluno: '))
    quantidade_de_notas += 1
    pergunta = input('Deseja lançar mais alguma nota? (s/n)')
    if pergunta == 's':
        pass
    else:
        sistema_acabou = True

nota_final = notas / quantidade_de_notas

print("""
    ----------------------------
    Notas globais: {}
    Quantidade de avaliações: {}
    Nota final: {}
    ----------------------------
""".format(notas, quantidade_de_notas, nota_final))
