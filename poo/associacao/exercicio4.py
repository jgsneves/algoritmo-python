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