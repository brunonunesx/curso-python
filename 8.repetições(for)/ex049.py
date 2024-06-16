num = int(input('Digite um número para vê sua tabuada: '))
final = int(input('Digite até aonde quer ir a tabuada: '))
print('_'*15)
print('Tabela do Número {}'.format(num))
print('_'*15)
for c in range (0, final+1):
    print('{} X {:2} = {}'.format(num, c, (num * c)))
print('_'*15)