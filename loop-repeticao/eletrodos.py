valor_da_tonelada = float(input('Informe o valor da tonelada: R$'))
quantidade_de_toneladas = 0

o_programa_acabou = False

while not o_programa_acabou:
    quantidade_de_toneladas = quantidade_de_toneladas + int(input('Informe a quantidade de toneladas: '))
    pergunta = input('Deseja informar mais toneladas? (s/n)')

    if pergunta == 's':
        pass
    else:
        o_programa_acabou = True

preco_final = quantidade_de_toneladas * valor_da_tonelada

print("""
    ---------------------------
    Preço da tonelada: R$ {}
    Quantidade de toneladas: {}

    Preço final: R$ {}
    ---------------------------
""".format(valor_da_tonelada, quantidade_de_toneladas, preco_final))