from contaCorrente import ContaCorrente
from pessoa import Pessoa

joao = Pessoa('Joao', 'Neves', '03/05/1989', 'masculino', '200.200.200-20')

conta = ContaCorrente('100', '5050', 12345, joao)

print("""
    Conta corrente de {} {}:
    Banco: {}
    Agencia: {}
    Conta: {}
    Senha: {}
    Saldo: {}
    -------------
    O titular da conta é {}
    Dados do titular:
    Data de nascimento: {}
    Gênero: {}
    CPF: {}
""".format(
    conta.titular.primeiro_nome,
    conta.titular.ultimo_nome,
    conta.banco,
    conta.agencia,
    conta.numero,
    conta.senha,
    conta.saldo,
    conta.titular,
    conta.titular.data_nascimento,
    conta.titular.genero,
    conta.titular.cpf
))
