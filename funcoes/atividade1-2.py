numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

def somarDoisNumeros(num1, num2):
    return num1 + num2

def subtrairDoisNumeros(num1, num2):
    return num1 - num2

def multiplicarDoisNumeros(primeiro, segundo):
    return primeiro * segundo

def multiplicarCincoNumeros(primeiro, segundo, terceiro, quarto, quinto):
    return primeiro * segundo * terceiro * quarto * quinto

def opereDoisNumeros(num1, num2, opcao):
    if opcao == 1:
        somarDoisNumeros(num1, num2)
    elif opcao == 2:
        subtrairDoisNumeros(num1, num2)
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        return num1 / num2

def dividirDoisNumeros(num1, num2):
    return num1 / num2

soma = somarDoisNumeros(numero_1, numero_2)
subtracao = subtrairDoisNumeros(numero_1, numero_2)
multiplicacao = multiplicarDoisNumeros(numero_1, numero_2)
divisao = dividirDoisNumeros(numero_1, numero_2)
mutiplicacao_de_cinco_numeros = multiplicarCincoNumeros(10, 20, 50, 60, 50)

print('A soma dos dois números é: ', soma)
print('A subtração dos dois números é: ', subtracao)
print('A multiplicação dos dois números é: ', multiplicacao)
print('A divisão dos dois números é: ', divisao)