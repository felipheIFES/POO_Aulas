print('\n******* NÚMERO PRIMO ******')

check = ''
contador = 0

while True: # o program ficará rodando até que entre o "break" e então sairá do while

    numero=int(input('\nDigite um numero inteiro: '))

    for i in range (1, numero+1):
        if numero % i == 0:
            contador += 1
        
    if contador == 2:
        check = 'é'
        contador = 0
    else:
        check = 'não é'
            
    print('\nO número', numero, '"',check,'"', 'primo')

    if check == 'não é':
        print('')
        break                        # break