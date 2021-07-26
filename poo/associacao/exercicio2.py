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
    
    def adicionarProduto(self, novo_produto):
        self.produtos.append(novo_produto)
        
    def removerProduto(self, nome_produto):
        for produto in self.produtos:
            if produto["nome"] == nome_produto:
                self.produtos.remove(produto)
    
            
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

carrinho_joao = CarrinhoCompras('João', "Rua de Cima", [], 0)

carrinho_joao.adicionarProduto(iphonex)
carrinho_joao.adicionarProduto(call_of_duty)
carrinho_joao.removerProduto("Iphone X")
print(carrinho_joao.valorTotal)

