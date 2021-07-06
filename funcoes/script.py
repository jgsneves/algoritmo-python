numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

def ordenarTresNumeros(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    menor = lista[0]
    meio = lista[1]
    maior = lista[2]
    
    return menor, meio, maior

menor, meio, maior = ordenarTresNumeros(numero1, numero2, numero3)

print('Os três números na ordem: ', menor, meio, maior)