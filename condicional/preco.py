produto1 = int(input('Digite o preço do produto 1: '))

produto2 = int(input('Digite o preço do produto 2: '))

produto3 = int(input('Digite o preço do produto 3: '))

if produto1 < produto2 and produto1 < produto3:
    print('Devemos comprar o produto 1!')
elif produto2 < produto1 and produto2 < produto3:
    print('Devemos comprar o produto 2!')
elif produto3 < produto1 and produto3 < produto2:
    print('Devemos comprar o produto 3!')
