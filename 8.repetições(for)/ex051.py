print('=='*13)
print('   10 TERMOS DE UMA PA     ')
print('=='*13)

pt = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a razão da PA: '))
ut = int(input('Até que número vc que ir: '))
utf = pt + (ut - 1)*razão
for c in range (pt, utf + razão, razão):
    print("{}".format(c),end='->')
print('Acabou')