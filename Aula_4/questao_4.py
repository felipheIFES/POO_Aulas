print('\nCÁLCULO DE ÍNDICE DE MASSA CORPORAL')
x=float(input('\nInforme seu peso: '))
y=float(input('Informe sua altura (em metros): '))

IMC = x/y**2
print(f'\nIMC= {IMC:.3f}') #para funcionar as casas decimais, tem que ter o "f" depois do número

if IMC<18.5:
    print('\nAbaixo do peso')
elif 18.5<=IMC<25:
    print('\nSaudável')
elif 25<=IMC<30:
    print('\nPeso em excesso')
elif 30<=IMC<35:
    print('\nObesidade Grau I') 
elif 35<=IMC<40:
    print('\nObesidade Grau II (severa)')         
elif IMC>=40:
    print('\nObesidade Grau III (mórbida)') 