def cadastro():
    name = input('Digite seu nome: ')
    idade = int(input('Sua idade: '))

    return name, idade

print('Iniciando cadastro....')
name, idade = cadastro()

print('Cadastro realizado com sucesso!')
print("""
    Seu nome: {}
    Sua idade: {}
""".format(name, idade))