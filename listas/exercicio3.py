def calcular_vogais(texto):
    vogais = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }
    for letra in texto:
        as_vogais = 'aeiou'
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra =="u":
            vogais[letra] += 1
            
    return vogais
            
palavra = input('Digite uma palavra: ')

print(calcular_vogais(palavra))
