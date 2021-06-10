import random

numero_escolhido = random.randrange(1,10)

numero_do_usuario = int(input('Digite um número: '))

while numero_do_usuario != numero_escolhido:
    if numero_do_usuario < numero_escolhido:
        print('Seu número é menor do que o número escolhido!')
        numero_do_usuario = int(input('Escolha um número maior: '))
    else:
        print('Seu número é maior do que o número escolhido!')
        numero_do_usuario = int(input('Escolha um número menor: '))
print('Parabéns! Você acertou o número escolhido!')
