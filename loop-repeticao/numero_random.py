import random

numero = random.randrange(1,10)
numero_do_usuario = int(input('Digite um numero:'))
while numero_do_usuario != numero:
    if numero_do_usuario > numero:
        print('Você escolheu um número maior do que eu escolhi!')
        numero_do_usuario = int(input('Tente outra vez: '))
    else:
        print('Você escolheu um número menor!')
        numero_do_usuario = int(input('Tente outra vez: '))
print('Parabéns você acertou!')