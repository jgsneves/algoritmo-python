class Produto:
    _nome = str()
    _preco = float()
    _estoque = int()

    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco
    
    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, novo_estoque):
        self._estoque = novo_estoque