oper=input('\nQual operação deseja realizar? (+ , - , * , /): ')
x=float(input('\nPrimeiro número:\n'))
y=float(input('Segundo número:\n'))

match oper:
    case '+':
        resultado=x+y
        print('\nResultado =',resultado)
    case '-':
        resultado=x-y
        print('\nResultado =',resultado)
    case '*':
        resultado=x*y
        print('\nResultado =',resultado)
    case '/':
        if y!=0:
            resultado=x/y
            print('\nResultado =',resultado)
        else:
            print('\nO divisor é "0"')
            print('\nOperação Impossível') 
    case _:
        print('\nOperação inválida! Operador ',oper)


""" comentar várias linha:
    ex.:
    resultado = None
    if resultado is note None:
"""