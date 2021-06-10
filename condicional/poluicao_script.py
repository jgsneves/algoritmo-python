indice_poluicao = input('Indice de poluicao atual: ')
indice_poluicao_numero_real = float(indice_poluicao)


if indice_poluicao_numero_real >= 0.3 and indice_poluicao_numero_real < 0.4:
    print('Empresas do grupo 1 devem suspender suas atividades')
elif indice_poluicao_numero_real >= 0.4 and indice_poluicao_numero_real < 0.5:
    print('Empresas dos grupos 1 e 2 devem suspender suas atividades')
else:
    print('Todos as empresas dos grupos 1, 2 e 3 devem suspender suas atividades')