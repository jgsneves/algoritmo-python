pacientes_sintomas_leves = 0
pacientes_assintomaticos = 0
pacientes_sintomas_graves = 0

for num in range(10):
    resposta = input('Qual quadro do paciente? (leve/assintomatico/grave)')

    if resposta == 'leve':
        pacientes_sintomas_leves += 1
        print('Paciente com sintoma leve registrado!')
    elif resposta == 'assintomatico':
        pacientes_assintomaticos += 1
        print('Paciente assintomático registrado!')
    elif resposta == 'grave':
        pacientes_sintomas_graves += 1
        print('Paciente com sintoma grave registrado!')
    else:
        print('Resposta inválida!')

percentual_leve = (pacientes_sintomas_leves / 10) * 100
percentual_assintomatico = (pacientes_assintomaticos / 10) * 100
percentual_grave = (pacientes_sintomas_graves / 10) * 100

print("""
    ---------------------
    Pacientes com sintomas leves: {}%
    Pacientes assintomáticos: {}%
    Pacientes com sintomas graves: {}%
    ---------------------
""".format(percentual_leve, percentual_assintomatico, percentual_grave))