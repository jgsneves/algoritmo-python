time1 = input('Digite o nome do time 1: ')
gol_time_1 = input('Quantos gols o time 1 fez? ')

time2 = input('Digite o nome do time 2: ')
gol_time_2 = input('Quantos gols o time 2 fez? ')

if gol_time_1 > gol_time_2:
    print('O {} foi vencedor!'.format(time1))
elif gol_time_1 < gol_time_2:
    print('O {} foi vencedor!'.format(time2))
else:
    print('A partida terminou em empate')
