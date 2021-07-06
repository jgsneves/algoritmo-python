numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

def ordenarTresNumeros(num1, num2, num3):
    menor = min(num1, num2, num3)
    meio = 0
    maior = max(num1, num2, num3)
    
    if num1 > menor and num1 < maior:
        meio = num1
        
    if num2 > menor and num2 < maior:
        meio = num2
        
    if num3 > menor and num3 < maior:
        meio = num3
    
    return menor, meio, maior

menor, meio, maior = ordenarTresNumeros(numero1, numero2, numero3)

print('Os três números na ordem: ', menor, meio, maior)