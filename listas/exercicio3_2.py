def contaVogais (string):
    string.lower()
    vogais = 'aeiou'
    return {vogal: string.count(vogal) for vogal in vogais}

texto = input('Insira seu texto: ')
print(contaVogais(texto))