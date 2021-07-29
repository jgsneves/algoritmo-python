class Produto:
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
    
    def valorTotal(self):
        return self.valor * self.quantidade
    
class CarrinhoCompras:
    def __init__(self, comprador, endereco, produtos, valorTotal):
        self.__valorTotal = valorTotal
        self.comprador = comprador
        self.endereco = endereco
        self.produtos = produtos
        
    @property
    def valorTotal(self):
        for produto in self.produtos:
            valor_de_produto = produto.valorTotal()
            self.__valorTotal += valor_de_produto
        return self.__valorTotal
        
    def adicionarProduto(self, novo_produto):
        self.produtos.append(novo_produto)
        
    def removerProduto(self, nome_produto):
        for produto in self.produtos:
            if produto["nome"] == nome_produto:
                self.produtos.remove(produto)
                
carrinho_joao = CarrinhoCompras('João', 'Rua de Cima', [], 0)

iphone_x = Produto('Iphone X', 5000, 1)
carrinho_joao.adicionarProduto(iphone_x)

jogo_panela = Produto('Jogo de panela', 200, 2)
carrinho_joao.adicionarProduto(jogo_panela)

samsung_a30s = Produto('Samsung A30s', 2000, 1)
carrinho_joao.adicionarProduto(samsung_a30s)

valor = carrinho_joao.valorTotal
print(valor)