numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
operacao = int(input("""
    -----------
    Deseja somar? digite 1
    Deseja subtrair? digite 2
    Deseja multiplicar? digite 3
    Deseja dividir? digite 4                 
"""))
resultado = 0

def somarDoisNumeros(num1, num2):
    return num1 + num2

def subtrairDoisNumeros(num1, num2):
    return num1 - num2

def multiplicarDoisNumeros(num1, num2):
    return num1 * num2

def dividirDoisNumeros(num1, num2):
    return num1 / num2

if operacao == 1:
    resultado = somarDoisNumeros(numero_1, numero_2)
elif operacao == 2:
    resultado = subtrairDoisNumeros(numero_1, numero_2)
elif operacao == 3:
    resultado = multiplicarDoisNumeros(numero_1, numero_2)
elif operacao == 4:
    resultado = dividirDoisNumeros(numero_1, numero_2)

print('O resultado é: ', resultado)
    