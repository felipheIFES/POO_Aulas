print('\nAUTOMAÇÃO NO SUPERMERCADO')

y = 0

x=float(input('\nPreço do produto: '))
if x != 0:
    y=float(input('Quantidade: '))
final=x*y

while x > 0 :

    x=float(input('\nPreço do produto: '))
    if x != 0:
        y=float(input('Quantidade: '))
    z=x*y

    final+=z

print('\nPara pagamento à VISTA: "1"')
print('Para pagamento à Prazo: "2"')
pagamento=int(input(': '))

if pagamento == 1:
    conta = 0.9 * final
    print('\nO valor de sua compra à vista ficou em :',conta)
else:
    parcelas = final / 5
    print('\nO valor de sua compra à prazo ficou em :',final,' e o valor das parcelas é de R$',parcelas)





