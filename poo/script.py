from endereco import Endereco
from cliente import Cliente

endereco_da_infinity = Endereco(
    '41700-000',
    'Alameda Salvador',
    1057,
    'Caminho das Árvores',
    'Salvador',
    'Bahia',
)

paulo = Cliente(
    'Paulo Fernandes',
    'paulo@email.com',
    '123456',
    endereco_da_infinity,
)

print("""
    -----------
    Nome do Cliente: {}
    Endereço: {}, {}, {}, {}, {}, {}    
""".format(
    paulo.nome, 
    paulo.endereco.rua,
    paulo.endereco.numero,
    paulo.endereco.bairro,
    paulo.endereco.cidade,
    paulo.endereco.estado,
    paulo.endereco.cep,
))
