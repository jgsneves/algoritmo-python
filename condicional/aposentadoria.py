#inicio

codigo_empregado = input('Código do empregado: ')

ano_nascimento = input('Ano de nascimento do empregado: ')
ano_nascimento_int = int(ano_nascimento)

ano_ingresso = input('Ano de ingresso na empresa: ')
ano_ingresso_int = int(ano_ingresso)

pode_aposentar = False

idade = 2021 - ano_nascimento_int
tempo_de_trabalho = 2021 - ano_ingresso_int

if idade >= 65:
    #primeira condição
    pode_aposentar = True
elif tempo_de_trabalho >= 30:
    #segunda cond
    pode_aposentar = True
elif idade >= 60 and tempo_de_trabalho >= 25:
    #terceira cond
    pode_aposentar = True

aposentadoria = ''

if pode_aposentar:
    aposentadoria = 'sim'
else:
    aposentadoria = 'não'

retorno = """
-------------------------------------------
Idade: {0} anos
Tempo de trabalho: {1} anos

Deve o trabalhador aposentar? {2}.
-------------------------------------------
"""
print(retorno.format(idade, tempo_de_trabalho, aposentadoria))

#fim