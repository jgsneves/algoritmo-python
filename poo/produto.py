class Produto:
    _nome = str()
    _preco = float()
    _estoque = int()

    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def getNome(self):
        return self.__nome

    @property
    def getPreco(self):
        return self.__preco

    @property
    def getEstoque(self):
        return self.__estoque

    @_nome.setter
    def setNome(self, nome):
        self.__nome = nome

    @_preco.setter
    def setPreco(self, novo_preco):
        self.__preco = novo_preco

    @_estoque.setter
    def setEstoque(self, novo_estoque):
        self._estoque = novo_estoque