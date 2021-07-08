lista = []

for rodada in range(10):
    numero = int(input('Digite o {}º número: '.format(rodada+1)))
    lista.append(numero)
    
for item in lista:
    if item % 2 != 0:
        print(item)
        
        
        
10 / 2