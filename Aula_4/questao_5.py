print('\nPEDRA PAPEL E TESOURA')

A=input('\nJogador "A", faça sua escolha e digite: pedra ou papel ou tesoura\n')
B=input('\nJogador "B", faça sua escolha e digite: pedra ou papel ou tesoura\n')

if (A=='pedra' and B=='pedra') or (A=='papel' and B=='papel') or (A=='tesoura' and B=='tesoura'):
    print('\n"EMPATE"')

elif A=='pedra' and B=='papel':
    print('\n"B" VENCEU!! B -',(B), ', ganha de A -', (A) )
elif A=='pedra' and B=='tesoura':
    print('\n"A" VENCEU!! A -',(A), ', ganha de B -', (B) )

elif A=='papel' and B=='tesoura':
    print('\n"B" VENCEU!! B -',(B), ', ganha de A -', (A) )
elif A=='papel' and B=='pedra':
    print('\n"A" VENCEU!! A -',(A), ', ganha de B -', (B) )

elif A=='tesoura' and B=='pedra':
    print('\n"B" VENCEU!! B -',(B), ', ganha de A -', (A) )
elif A=='tesoura' and B=='papel':
    print('\n"A" VENCEU!! A -',(A), ', ganha de B -', (B) )



#print(x, end=' ')