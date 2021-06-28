from produto import Produto

chaveiro = Produto('Chaveiro', 2.50, 200)

print('antes', chaveiro.preco)

chaveiro.preco = 200


print('depois', chaveiro.preco)