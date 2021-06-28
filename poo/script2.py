from carrinho import Carrinho
from produto import Produto
from endereco import Endereco

endereco_da_infinity = Endereco(
    '41700-000',
    'Alameda Salvador',
    1057,
    'Caminho das Árvores',
    'Salvador',
    'Bahia',
)

controle = Produto(
    'Controle',
    459,
    2,
)

relogio = Produto(
    'Galaxy',
    279,
    1,
)

produtos = [controle, relogio]

carrinho_de_joao = Carrinho(
    produtos,
    endereco_da_infinity,
)

valor_final = carrinho_de_joao.retornarValorFinal()

print(valor_final)
