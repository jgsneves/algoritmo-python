class CarrinhoCompras:
    def __init__(self, comprador, endereco, produtos, valorTotal):
        self.__valorTotal = valorTotal
        self.comprador = comprador
        self.endereco = endereco
        self.produtos = produtos
        
    @property
    def valorTotal(self):
        for produto in self.produtos:
            self.__valorTotal += produto["valor"] * produto["quantidade"]
        return self.__valorTotal
    
            
iphonex = {
    "nome": "Iphone X",
    "valor": 5000,
    "quantidade": 2,
}

call_of_duty = {
    "nome": "Call of Duty",
    "valor": 200,
    "quantidade": 1,
}

carrinho_joao = CarrinhoCompras('João', "Rua de Cima", [iphonex, call_of_duty], 0)
print(carrinho_joao.valorTotal)
