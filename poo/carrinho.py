from endereco import Endereco

class Carrinho:
    _produtos = list()
    _valorFinal = float()
    _endereco = str()
    
    def __init__(self, produtos, endereco):
        if isinstance(produtos, list) and isinstance(endereco, Endereco):
            self._produtos = produtos
            self._endereco = endereco
        else:
            print('Forneça uma lista de produtos e um endereço válido!')

    def retornarValorFinal(self):
        for produto in self._produtos:
            self._valorFinal = self._valorFinal + (produto.preco * produto.quantidade)
        return self._valorFinal