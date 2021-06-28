import random

class Endereco:
    def __init__(self, cep, rua, numero, bairro, cidade, estado):
        self._cep = cep
        self._rua = rua
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
        self._estado = estado
        self.__id = random.randrange(0, 100000)
        
    @property
    def cep(self):
        return self._cep
    
    @cep.setter
    def cep(self, novo_cep):
        self._cep = novo_cep
    
    @property
    def rua(self):
        return self._rua
    
    @rua.setter
    def rua(self, nova_rua):
        self._rua = nova_rua
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero
        
    @property
    def bairro(self):
        return self._bairro
    
    @bairro.setter
    def bairro(self, novo_bairro):
        self._bairro = novo_bairro
        
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        self._cidade = nova_cidade
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, novo_estado):
        self._estado = novo_estado
        
    @property
    def id(self):
        return self.__id
    