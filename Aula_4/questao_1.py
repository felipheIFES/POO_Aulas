numero=int(input('\nDigite um número para verificação\n'))

resto = numero % 2

if resto == 0:
    print(f'\nO número {numero} é Par')
else:
    print('\nÍMPAR')



#exemplo de if else em uma linha
x=10
y=8
x = x/y if y > x else 0