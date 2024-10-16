x=int(input('\nDigite o primeiro número para verificação (X):\n'))
y=int(input('Digite o segundo número para verificação (Y):\n'))

if x>y: #and x>10:
    print(f'\nx({x}) é maior do que y({y})')
elif y>x:
    print(f'\ny({y}) é maior do que x({x})')   
else:
    print(f'\nx({x}) e y({y}) são iguais')