print('\nSOMATÓRIO DE N.s ÍMPARES ATÉ 1000\n')

x=0
total=0

while x <= 1000:
    if x%2 != 0:
        total += x

    x += 1

print ('Somatório =',total,'\n')