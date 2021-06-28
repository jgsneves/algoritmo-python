class Produto:
    _nome = str()
    _preco = float()
    _quantidade = int()

    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

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
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade
        
