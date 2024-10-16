soma_numeros = 0

while True:
    numero = int(input('\nDigite o numero para soma: '))

    if numero == 0:
        break

    soma_numeros += numero    

print('\nA soma dos numeros é', soma_numeros)